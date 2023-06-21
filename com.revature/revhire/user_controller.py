from random import randint
import strawberry
from strawberry.fastapi import GraphQLRouter
from collections import Counter
from typing import Optional
from model.user import users,User
from dto.doesNotExistResponse import DoesNotExist
from dto.userRequest import UserRequest



def user_resolver(id: int | None = None) -> list[users]:

    if id:
        return [u for u in list(users.values()) if id == u.id]

    return list(users.values())

def userResolverForFirstName(firstName: str | None = None) -> list[users]:

    if id:
        return [u for u in list(users.values()) if firstName == u.firstName]

    return list(users.values())


Response = strawberry.union(
    "GetUserResponse", [User,DoesNotExist]
)

def add_user(input:UserRequest)->UserRequest:
    user=User(
        id=randint(1,1000),
        title=input.title,
        firstName=input.firstName,
        lastName=input.lastName,
        email=input.email,
        address=input.address,
        contactNumber=input.contact_number,
        designation=input.designation,
        dob=input.dob,
        gender=input.gender,
        password=input.password,
        role=input.role,

    )
    users[user.id]=user
    return user

@strawberry.type
class Query:
    users:list[User]=strawberry.field(resolver=user_resolver)
    user:list[User]=strawberry.field(resolver=userResolverForFirstName)



@strawberry.input
class Mutation:
    add_user:User = strawberry.field(resolver=add_user)

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQLRouter(schema)

