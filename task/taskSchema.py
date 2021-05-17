from pydantic import BaseModel

from user import userSchemas


class Task(BaseModel):
    title: str
    description: str
    completed: bool
    creator: userSchemas.ShowUser

    class Config:
        orm_mode = True


class SimpleTask(BaseModel):
    title: str
    description: str
    completed: bool

    class Config:
        orm_mode = True
