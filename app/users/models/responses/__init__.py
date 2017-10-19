from marshmallow import post_load
from app.serializer import BaseSchema
from app.users.models import User


class UserSchema(BaseSchema):
    class Meta:
        model = User

    @post_load
    def make_user(self, data):
        return User(**data)
