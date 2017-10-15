from app.users.models import User
from utils.http import Get, Post, Put, Delete


class UserController:

    @Get('/user/<int:user_id>', endpoint='user')
    def get_user_by_id(user_id):
        print(user_id)
        return "YOU WANTED {}".format(user_id)

    @Get('/user/<string:username>', endpoint='user')
    def get_user_by_username(username):
        return "YOU WANTED {}".format(username)

    @Get('/users', endpoint='user')
    def get_all_users(self):
        return "YOU WANTED ALL"

    @Post('/users', body=User, endpoint='user')
    def new(user: User):
        print("called some method with {}".format(user))
        user.save()
        return "Helloooo {}".format(user.username)

    @Delete('/user/<string:username>', body=User, endpoint='user')
    def delete_user_by_id(username):
        print(username)
        return "YOU WANTED {}".format(username)

    @Delete('/user/<int:user_id>', body=User, endpoint='user')
    def delete_user_by_username(user_id):
        print(user_id)
        return "YOU WANTED {}".format(user_id)


