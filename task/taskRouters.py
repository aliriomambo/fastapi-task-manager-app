from fastapi import APIRouter, Depends, status

from auth import oauth2
from task import taskSchema, task_repository
from user import userSchemas
from typing import List

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


@router.get('/')
def get_tasks(current_user: userSchemas.PublicUser = Depends(oauth2.get_current_user), response_model=List[taskSchema.Task]):
    return task_repository.get_all_tasks(current_user.id)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: taskSchema.SimpleTask, current_user: userSchemas.PublicUser = Depends(oauth2.get_current_user)):
    return task_repository.create_task(request, current_user.id)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=taskSchema.Task)
def get_tasks_by_id(task_id: str, current_user: userSchemas.PublicUser = Depends(oauth2.get_current_user)):
    return task_repository.get_task_by_id(task_id, current_user.id)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_task_by_id(task_id: str,
                      current_user: userSchemas.PublicUser = Depends(oauth2.get_current_user)):
    return task_repository.delete_task_by_id(task_id, current_user.id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_task_by_id(task_id: int, request: taskSchema.SimpleTask,
                      current_user: userSchemas.PublicUser = Depends(oauth2.get_current_user)):
    return task_repository.update_task_by_id(task_id, request, current_user.id)
