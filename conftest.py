import os
import tempfile
import sqlalchemy

import pytest
from db import db
from app import app

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:shopper@localhost:3306/shoppertest?charset=utf8mb4"

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

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])