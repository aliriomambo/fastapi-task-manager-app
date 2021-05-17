from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    creator = relationship("User", back_populates="tasks")
