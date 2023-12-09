import strawberry
import uvicorn
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI
from typing import Optional

from .config import DatabaseSession
from .Graphql.query import Query
from .Graphql.mutation import Mutation

db = DatabaseSession()

app = FastAPI()

@app.on_event("startup")
async def startup():
  await db.create_all()

@app.on_event("shutdown")
async def shutdown():
  await db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/health")
async def health_check():
    # Perform health checks here
    # Return a JSON response indicating the health status
    return {"status": "ok"}

# Add graphql endpoint
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
