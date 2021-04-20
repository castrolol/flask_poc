import uuid
from sqlalchemy import Column, String, Binary, Boolean 
from db import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = Column(Binary, primary_key=True)
    name = Column(String)
    done = Column(Boolean)
    color = Column(String)

    def as_dict(self):
        res = dict((c.name,
            getattr(self, c.name))
                for c in self.__table__.columns)

        res["id"] = uuid.UUID(bytes=res["id"])
        return res