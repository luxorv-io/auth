from app.users.models import User
from app.users.models.responses import UserSchema


class UserService(object):

    def __init__(self):
        self.user_schema = UserSchema()
        self.users_schema = UserSchema(many=True)

    def get_user_by(self, **kwargs):
        user = User.query.filter_by(**kwargs).first()
        return self.user_schema.jsonify(user)

    def get_all_users(self):
        users = User.query.all()
        return self.users_schema.jsonify(users)

    def new_user(self, user):
        user.save()
        return self.user_schema.jsonify(user)

    def delete_user_by(self, **kwargs):
        user = User.query.filter_by(**kwargs).first()
        user.delete()
        return True, 200
