import strawberry
from typing import List
from education import Education
from expereince import Experience

@strawberry.type
class Education:
    id:int
    jonseekerId:int
    objective:str
    experience: List[int]
    education:List[Education]
    skills:List[Experience]


    