from app import ma
from app import db
from utils import db.BaseModel


class User(BaseModel):
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.Email)
    username = db.Column(db.String)
    password = db.Column(db.String)


class UserSchema(ma.ModelSchema):
    class Meta:
	model = User

