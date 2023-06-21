import strawberry


@strawberry.type
class Education:
    id:int
    userId:int
    fromDate:str
    tillDate:str
    type:str
    specialization:str


