from app import ma
from app import db
from utils import db.BaseModel


class User(BaseModel):
    username = db.Column(db.String)
    email = db.Column(db.Email)


class UserSchema(ma.ModelSchema):
    class Meta:
		model = User

