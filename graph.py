import graphene
from fastapi import FastAPI, APIRouter
from starlette.graphql import GraphQLApp
graph_router = APIRouter()


app = FastAPI(title='ContactQL', description='GraphQL Contact APIs', version='0.1')



class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))


    def resolve_hello(self, info, name):
            return "Hello " + name


@graph_router.get("/")
async def root():
    return {"message": "Contact Applications!"}

graph_router.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))