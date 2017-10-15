from app import server
from marshmallow import post_load

from app.users.models import User


class UserSchema(server.marshmallow.ModelSchema):
    class Meta:
        model = User

    @post_load
    def make_user(self, data):
        return User(**data)
