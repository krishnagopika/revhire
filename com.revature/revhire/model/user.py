import strawberry

from enum import Enum

@strawberry.type
class User:
    id:int
    email:str
    password:str
    title:str
    firstName:str
    lastName:str
    dob:str
    contactNumber:str
    address: str
    gender: str
    designation:str
    role:"Role"

@strawberry.enum
class Role(Enum):
    JOBSEEKER = "jobseeker"
    EMPLOYER = "employer"

user1 = User(
    id=1,
    email="user1@example.com",
    password="pass123",
    title="Mr",
    firstName="John",
    lastName="Doe",
    dob="1990-01-01",
    contactNumber="1234567890",
    address="123 Main St",
    gender="M",
    designation="Engineer",
    role=Role.JOBSEEKER
)

user2 = User(
    id=2,
    email="user2@example.com",
    password="pass456",
    title="Ms",
    firstName="Jane",
    lastName="Smith",
    dob="1995-05-10",
    contactNumber="9876543210",
    address="456 Elm St",
    gender="F",
    designation="Manager",
    role=Role.EMPLOYER
)

users = {
    user1.id: user1,
    user2.id: user2
}

  

    
