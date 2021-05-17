from datetime import timedelta

from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import auth.oauth2
from db.database import get_db
from user import userModels
from .oauth2 import create_access_token

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(userModels.User).filter(userModels.User.email == request.username).one_or_none()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    if not auth.oauth2.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
