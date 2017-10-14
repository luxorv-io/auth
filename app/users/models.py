from app import ma
from app import db
from marshmallow import post_load
from utils.db import BaseModel


class User(BaseModel):
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
        self.email = kwargs.get('email', '')
        self.username = kwargs.get('username', '')
        self.password = kwargs.get('password', '')

    def __str__(self):
        return str(dict(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            password=self.password,
            username=self.username
        ))


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    @post_load
    def make_user(self, data):
        return User(**data)
