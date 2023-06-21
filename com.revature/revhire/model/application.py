import strawberry
from enum import Enum

@strawberry.type
class Application:
    id:int
    userId:int
    jobId:int
    resumeId:int
    appliedOn:str
    status:Status

@strawberry.enum
class Status(Enum):
    SUBMITTED="Submitted"
    InReview="In review"
    Accepted= "Accepted"
    Rejected="Rejected"


