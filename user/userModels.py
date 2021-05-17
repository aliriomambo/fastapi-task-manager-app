from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from db.database import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (UniqueConstraint("email"),)
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    email = Column(String)

    tasks = relationship('Task', back_populates="creator")
