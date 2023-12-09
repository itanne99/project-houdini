from ..Model.user import User
from ..Repository.user import UserRepository
from ..schema import CreateUserInput, UpdateUserInput, UserType

def map_user_to_user_type(user: User) -> UserType:
    return UserType(
        id=user.id,
        firstName=user.firstName,
        lastName=user.lastName,
        email=user.email,
        active=user.active,
        guid=user.guid,
        createDate=user.createDate,
        updateDate=user.updateDate,
        additionalInfo=user.additionalInfo
    )

class UserService:

  @staticmethod
  async def create_user(user_data: CreateUserInput):
    if await UserRepository.doesUserExist(user_data.email):
      return {
        'status': 409,
        'message': f'User already exists with email {user_data.email}'
      }
    user = User(
      firstName=user_data.firstName,
      lastName=user_data.lastName,
      email=user_data.email,
      password=user_data.password,
      additionalInfo=user_data.additionalInfo
    )

    await UserRepository.create(user)

    return map_user_to_user_type(user)

  @staticmethod
  async def get_all_users():
    list_user = await UserRepository.get_all()
    return [map_user_to_user_type(user) for user in list_user]

  @staticmethod
  async def get_by_attribute(attribute: str, user_id: int):
    user = await UserRepository.get_by_attribute(attribute, user_id)
    return map_user_to_user_type(user)

  @staticmethod
  async def delete(user_guid: str):
    await UserRepository.delete(user_guid)
    return {'message': f'Successfully deleted data by id {user_guid}'}

  @staticmethod
  async def activate(user_guid: str):
    await UserRepository.activate_user(user_guid)
    return {'message': f'Successfully activated user @ guid {user_guid}'}

  @staticmethod
  async def deactivate(user_guid: str):
    await UserRepository.deactivate_user(user_guid)
    return {'message': f'Successfully deactivated user @ guid {user_guid}'}

  @staticmethod
  async def update(user_guid: str, user_data: UpdateUserInput):
    await UserRepository.update_user_info(user_guid, user_data)
    return {'message': f'Successfully updated data by id {user_guid}'}

  #Update user password, use update_user_password(user_guid: str, password: str)
  async def update(user_guid: str, password: str):
    await UserRepository.update_user_password(user_guid, password)
    return {'message': f'Successfully updated user\'s password by id {user_guid}'}