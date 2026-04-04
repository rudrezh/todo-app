from app.models.todo import Todo
from app.db.database import db_session

class TodoService:

    @staticmethod
    def get_all():
        return [t.to_dict() for t in db_session.query(Todo).all()]

    @staticmethod
    def create(task):
        todo = Todo(task=task)
        db_session.add(todo)
        db_session.commit()
        return todo.to_dict()

    @staticmethod
    def delete(todo_id):
        todo = db_session.query(Todo).filter_by(id=todo_id).first()
        if not todo:
            return False

        db_session.delete(todo)
        db_session.commit()
        return True