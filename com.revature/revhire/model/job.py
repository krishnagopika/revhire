import strawberry

from typing import List

@strawberry.type
class Job:
    id:int
    creatorId:int
    companyName:str
    logo:str
    createdOn:str
    designation:str
    location:str
    description:str
    skills: List[str]
