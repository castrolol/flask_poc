from flask import Flask, request, jsonify
from todos.service import all_todos, create_todo, update_todo

def todos_module(app):

    @app.route("/todos", methods=["GET"])
    def get_all():
        todos = all_todos()
        return jsonify(todos=todos)

    @app.route("/todos", methods=["POST"])
    def insert():
        task = create_todo(request.json)
        return task

    @app.route("/todos/<todo_id>", methods=["PUT"])
    def update(todo_id):
        result = update_todo(todo_id, request.json)
        return  result
