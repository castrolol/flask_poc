import os
from dotenv import load_dotenv
load_dotenv(".env.test")
import sqlalchemy
import pytest
from infra.db import db
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")

    eng = sqlalchemy.create_engine(
        "mysql+pymysql://root:shopper@localhost:3306",
        isolation_level='AUTOCOMMIT'
    )

    eng.execute("DROP DATABASE IF EXISTS shoppertest")
    eng.execute("CREATE DATABASE shoppertest")

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()
