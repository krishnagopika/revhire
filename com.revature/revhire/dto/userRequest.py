import strawberry

from model.user import Role

@strawberry.input
class UserRequest:
    email:str
    password:str
    title:str
    firstName:str
    lastName:str
    dob:str
    contact_number:str
    address: str
    gender: str
    designation:str
    role:"Role"

