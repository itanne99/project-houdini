import os
from dotenv import load_dotenv

from ..Model.user import User
from ..config import db
from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete
import datetime
from cryptography.fernet import Fernet

def encrypt(string: str):
  load_dotenv()
  fernet = Fernet(os.getenv('ENCRYPTION_KEY'))
  return fernet.encrypt(string.password.encode())

def decrypt(string: str):
  load_dotenv()
  fernet = Fernet(os.getenv('ENCRYPTION_KEY'))
  return fernet.decrypt(string).decode()

class UserRepository:
    @staticmethod
    async def create(user_data: User):
        async with db as session:
            async with session.begin():
                user_data.password = encrypt(user_data.password)
                session.add(user_data)

            await db.commit_rollback()

    @staticmethod
    async def get_all():
        async with db as session:
            query = select(User)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def get_by_attribute(attribute: str, value: Any):
        async with db as session:
            stmt = select(User).where(getattr(User, attribute) == value)
            result = await session.execute(stmt)
            user = result.scalars().first()
            user.password = decrypt(user.password)
            return user

    @staticmethod
    async def doesUserExist(user_email: str):
        async with db as session:
            stmt = select(User).where(User.email == user_email)
            result = await session.execute(stmt)
            exists = result.scalars().first() is not None

            return exists

    @staticmethod
    async def delete(user_guid: str):
        async with db as session:
            # Delete user record
            query = delete(User).where(User.guid == user_guid)
            await session.execute(query)

            # Comment out the lines related to deleting data from other tables
            # query = delete(OtherTable).where(User.guid == user_guid)
            # await session.execute(query)

            await db.commit_rollback()

    @staticmethod
    async def activate_user(user_guid: str):
        async with db as session:
            stmt = select(User).where(User.guid == user_guid)
            result = await session.execute(stmt)

            user = result.scalars().first()
            user.active = True
            user.updateDate = datetime.datetime.utcnow()

            query = update(User).where(User.guid == user_guid).values(
                active=user.active, updateDate=user.updateDate
            ).execution_options(synchronize_session="fetch")

            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def deactivate_user(user_guid: str):
        async with db as session:
            stmt = select(User).where(User.guid == user_guid)
            result = await session.execute(stmt)

            user = result.scalars().first()
            user.active = False
            user.updateDate = datetime.datetime.utcnow()

            query = update(User).where(User.guid == user_guid).values(
                active=user.active, updateDate=user.updateDate
            ).execution_options(synchronize_session="fetch")

            await session.execute(query)
            await db.commit_rollback()

    async def update_user_info(user_guid: str, user_data: User):
        async with db as session:
            stmt = select(User).where(User.guid == user_guid)
            result = await session.execute(stmt)

            user = result.scalars().first()
            if user:
                user.email = user_data.email
                user.firstName = user_data.firstName
                user.lastName = user_data.lastName
                user.updateDate = datetime.datetime.utcnow()

                query = update(User).where(User.guid == user_guid).values(
                    email=user.email, firstName=user.firstName, lastName=user.lastName, updateDate=user.updateDate
                ).execution_options(synchronize_session="fetch")

                await session.execute(query)
                await db.commit_rollback()

    async def update_user_password(user_guid: str, password: str):
        async with db as session:
            stmt = select(User).where(User.guid == user_guid)
            result = await session.execute(stmt)

            user = result.scalars().first()
            if user:
                user.password = encrypt(password)

                query = update(User).where(User.guid == user_guid).values(
                    password=user.password
                ).execution_options(synchronize_session="fetch")

                await session.execute(query)
                await db.commit_rollback()