from dotenv import load_dotenv
import os
load_dotenv()
import uuid
from flask import Flask, jsonify
from infra.db import db

from todos.routes import todos_module

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)

@app.route("/")
def index():
    item = db.session.execute("SELECT DATABASE() FROM DUAL;").first()
    print(item[0])
    return item[0]

todos_module(app)
