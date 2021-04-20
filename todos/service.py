import uuid
from db import db
from todos.models.Task import Task

def all_todos():
    todos = Task.query.all()
    return [todo.as_dict() for todo in todos]

def create_todo(todo_dict):
    task = Task(**todo_dict)

    db.session.add(task)
    db.session.commit()

    return task.as_dict()

def update_todo(id, todo_dict):
    todo = Task.query.filter_by(id=id).one()

    todo.name = todo_dict["name"]
    todo.color = todo_dict["color"]

    db.session.commit()

    result = todo.as_dict() if todo else None
    return result