from fastapi import FastAPI

from auth import authRouters
from db.database import engine
from task import task_model, taskRouters
from user import userModels, userRouters

task_model.Base.metadata.create_all(engine)
userModels.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(taskRouters.router)
app.include_router(userRouters.router)
app.include_router(authRouters.router)
