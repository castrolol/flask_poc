import uuid
from infra.db import db
from todos.models.Task import Task


def all_todos():
    todos = Task.query.all()
    return todos

def create_todo(task):
    db.session.add(task)
    db.session.commit()
    return task

def update_todo(id, todo_dict):
    todo = Task.query.filter_by(id=id).one()

    todo.name = todo_dict["name"]
    todo.color = todo_dict["color"]

    db.session.commit()

    return todo