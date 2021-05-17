from fastapi import status, HTTPException, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import auth.oauth2
from db.database import get_db, SessionLocal
from user import userSchemas, userModels


def create_user(request: userSchemas.User):
    db:Session = SessionLocal()
    new_user = userModels.User(name=request.name, email=request.email, password=auth.oauth2.bcrypt(request.password))

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return new_user


def get_user_by_email(email: str, db: Session):
    user = db.query(userModels.User).filter(userModels.User.email == email).one_or_none()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user
