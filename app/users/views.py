from app.users.models import User
from app.users.services import UserService
from utils.http import get, post, delete


class UserController:

    @get('/user/<int:user_id>')
    def get_user_by_id(user_id, service: UserService):
        return service.get_user_by(id=user_id)

    @get('/user/<string:username>')
    def get_user_by_username(username, service: UserService):
        return service.get_user_by(username=username)

    @get('/users')
    def get_all_users(service: UserService):
        return service.get_all_users()

    @post('/users', body=User)
    def new(user: User, service: UserService):
        return service.new_user(user)

    @delete('/user/<string:username>', body=User)
    def delete_user_by_id(user_id, service: UserService):
        return service.delete_user_by(id=user_id)

    @delete('/user/<int:user_id>', body=User)
    def delete_user_by_username(username, service: UserService):
        return service.delete_user_by(username=username)
