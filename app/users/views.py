from app.users.models import User
from utils.http import Get, Post, Put, Delete


class UserResource:

    @Get('/user/<int:user_id>', endpoint='user-resource')
    def get_user_by_id(user_id):
        print(user_id)
        return "YOU WANTED {}".format(user_id)

    @Get('/user/<string:username>', endpoint='user-resource')
    def get_user_by_username(username):
        return "YOU WANTED {}".format(username)

    @Get('/users', endpoint='user-resource')
    def get_all_users():
        return "YOU WANTED ALL"

    @Post('/users', body=User, endpoint='user-resource')
    def new(user):
        print("called some method with {}".format(user))
        return "Helloooo {}".format(user.username)

    @Delete('/user/<string:username>', body=User, endpoint='user-resource')
    def delete_user_by_id(username):
        print(username)
        return "YOU WANTED {}".format(username)

    @Delete('/user/<int:user_id>', body=User, endpoint='user-resource')
    def delete_user_by_username(user_id):
        print(user_id)
        return "YOU WANTED {}".format(user_id)


