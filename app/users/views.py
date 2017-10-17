from app.users.models import User
from utils.http import get, post, put, delete


class UserController:

    @get('/user/<int:user_id>', endpoint='user')
    def get_user_by_id(user_id):
        print(user_id)
        return "YOU WANTED {}".format(user_id)

    @get('/user/<string:username>', endpoint='user')
    def get_user_by_username(username):
        return "YOU WANTED {}".format(username)

    @get('/users', endpoint='user')
    def get_all_users(self):
        return "YOU WANTED ALL"

    @post('/users', body=User, endpoint='user')
    def new(user: User):
        print("called some method with {}".format(user))
        user.save()
        return "Helloooo {}".format(user.username)

    @delete('/user/<string:username>', body=User, endpoint='user')
    def delete_user_by_id(username):
        print(username)
        return "YOU WANTED {}".format(username)

    @delete('/user/<int:user_id>', body=User, endpoint='user')
    def delete_user_by_username(user_id):
        print(user_id)
        return "YOU WANTED {}".format(user_id)


