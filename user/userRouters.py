from fastapi import APIRouter

from user import userSchemas, user_repository

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.post('/', response_model=userSchemas.ShowUser)
def create_user(request: userSchemas.User):
    return user_repository.create_user(request)
