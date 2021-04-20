import uuid
from flask import Flask
from db import db

from todos.routes import todos_module

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:shopper@localhost:3306/test?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)

@app.route("/")
def index():
    return "ok!"

todos_module(app)