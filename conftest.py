import os
from dotenv import load_dotenv
load_dotenv(".env.test")
import sqlalchemy
import pytest
from infra.db import db
from infra.config import database_uri
from app import app

@pytest.fixture
def client():
  
    init_test_database()

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()


def init_test_database():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri()

    eng = sqlalchemy.create_engine(
        "mysql+pymysql://{user}:{password}@{host}:{port}".format(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        ),
        isolation_level='AUTOCOMMIT'
    )

    eng.execute("DROP DATABASE IF EXISTS " + os.getenv("DB_DATABASE"))
    eng.execute("CREATE DATABASE " + os.getenv("DB_DATABASE"))
    