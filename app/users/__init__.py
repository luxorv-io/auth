from flask import Blueprint
from app.users.services import UserService

users = Blueprint('users', __name__)


from app.users.views import UserController

