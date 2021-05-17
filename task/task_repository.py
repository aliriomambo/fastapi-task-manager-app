from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from db.database import SessionLocal
from task import taskSchema, task_model


def get_all_tasks(user_id: int):
    db: Session = SessionLocal()
    tasks = db.query(task_model.Task).filter(task_model.Task.user_id == user_id).all()
    return tasks


def get_task_by_id(task_id, user_id: int):
    db: Session = SessionLocal()
    task = db.query(task_model.Task).filter(task_model.Task.id == task_id).filter(task_model.Task.user_id == user_id)

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    return task


def create_task(request: taskSchema.SimpleTask, user_id: int):
    db: Session = SessionLocal()
    new_task = task_model.Task(title=request.title, description=request.description, completed=request.completed,
                               user_id=user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def delete_task_by_id(task_id: str, user_id: int):
    db: Session = SessionLocal()
    task = db.query(task_model.Task).filter(task_model.Task.id == task_id).filter(task_model.Task.user_id == user_id)
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    task.delete(synchronize_session=False)
    db.commit()
    return status.HTTP_200_OK


def update_task_by_id(task_id: int, request: taskSchema.SimpleTask, user_id: int):
    db: Session = SessionLocal()
    task = db.query(task_model.Task).filter(task_model.Task.id == task_id).filter(
        task_model.Task.user_id == user_id).one_or_none()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    task.description = request.description
    task.title = request.title
    task.completed = request.completed
    db.commit()
    db.refresh(task)
    return status.HTTP_200_OK
