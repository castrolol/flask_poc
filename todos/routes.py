from flask import Flask, request, jsonify
from todos.service import all_todos, create_todo, update_todo
from todos.models.Task import Task
def todos_module(app):

    @app.route("/todos", methods=["GET"])
    def get_all():
        todos = all_todos()
        return jsonify(todos=[todo.as_dict() for todo in todos])

    @app.route("/todos", methods=["POST"])
    def insert():
        task = create_todo(Task(**request.json))
        return task.as_dict()

    @app.route("/todos/<todo_id>", methods=["PUT"])
    def update(todo_id):
        result = update_todo(todo_id, request.json)
        return  result.as_dict()
