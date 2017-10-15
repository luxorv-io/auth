from sqlalchemy import Column, String
from app.database import BaseModel
from app import server


class User(BaseModel):

    __tablename__ = 'users'

    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(120))
    username = Column(String(120))
    password = Column(String(120))

    def __init__(self, **kwargs):
        super().__init__()

    def save(self):
        server.db_session.add(self)
        server.db_session.commit()

    def update(self):
        server.db_session.commit()

    @staticmethod
    def get(**kwargs):
        return User.query.filter_by(**kwargs).first()

    @staticmethod
    def get_all(**kwargs):
        return User.query.filter_by(**kwargs).all()

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return str(dict(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            password=self.password,
            username=self.username
        ))
