import strawberry


@strawberry.type
class DoesNotExist:
    id: int 
    message: str