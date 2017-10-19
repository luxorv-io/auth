from app.users.models import User
from app.users.models.responses import UserSchema
from flask import jsonify


class UserService(object):

    def __init__(self):
        self.user_schema = UserSchema()
        self.users_schema = UserSchema(many=True)

    def get_user_by(self, **kwargs) -> User:
        user = User.query.filter_by(**kwargs).first()
        return jsonify(self.user_schema.dump(user).data)

    def get_all_users(self):
        users = User.query.all()
        return jsonify(self.users_schema.dump(users).data)

    def new_user(self, user):
        user.save()
        return jsonify(self.user_schema.dump(user).data)

    def delete_user_by(self, **kwargs):
        user = User.query.filter_by(**kwargs).first()
        user.delete()
        return True
