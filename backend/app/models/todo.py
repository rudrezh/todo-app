from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)

    def to_dict(self):
        return {"id": self.id, "task": self.task}