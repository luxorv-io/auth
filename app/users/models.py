from sqlalchemy import Column, String
from app.database import BaseModel
from utils import inject_session


class User(BaseModel):

    __tablename__ = 'users'

    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(120))
    username = Column(String(120))
    password = Column(String(120))

    def __init__(self, **kwargs):
        self.first_name = kwargs.pop('first_name', '')
        self.last_name = kwargs.pop('last_name', '')
        self.email = kwargs.pop('email', '')
        self.username = kwargs.pop('username', '')
        self.password = kwargs.pop('password', '')

    @inject_session
    def save(self, session):
        session.add(self)
        session.commit()

    @inject_session
    def update(self, session):
        session.commit()

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
