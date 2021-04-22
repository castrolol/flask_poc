from dotenv import load_dotenv
import os
load_dotenv()
from flask import Flask, jsonify
from infra.db import db
from infra.config import database_uri
from todos.routes import todos_module

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)

@app.route("/")
def index():
    return "ok"

todos_module(app)
