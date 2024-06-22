from src.db import Base

from sqlalchemy import Column, Integer, String, DateTime, Text

from datetime import datetime

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    finished_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)