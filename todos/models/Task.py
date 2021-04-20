import uuid
from sqlalchemy import Column, String, Boolean 
from db import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = Column(String(40), primary_key=True)
    name = Column(String(40))
    done = Column(Boolean)
    color = Column(String(20))

    def as_dict(self):
        res = dict((c.name,
            getattr(self, c.name))
                for c in self.__table__.columns)
        
        return res