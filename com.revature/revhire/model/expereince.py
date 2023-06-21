import strawberry

@strawberry.type
class Experience:
    id:int
    userId:int
    fromDate:str
    tillDate:str
    designation:str
    description:str

