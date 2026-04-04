from flask import Blueprint, request, jsonify
from app.services.todo_service import TodoService

todo_bp = Blueprint("todos", __name__)

@todo_bp.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(TodoService.get_all())

@todo_bp.route("/todos", methods=["POST"])
def add_todo():
    data = request.json
    if not data or "task" not in data:
        return jsonify({"error": "Invalid input"}), 400

    return jsonify(TodoService.create(data["task"])), 201

@todo_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    if TodoService.delete(todo_id):
        return jsonify({"msg": "deleted"})
    return jsonify({"error": "not found"}), 404