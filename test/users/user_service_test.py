from unittest import TestCase

from app.users.services import UserService
from app.users.models import User
from app.users.models.responses import UserSchema

from test import test_app, set_up_database, tear_down_database, set_up_serializer
from test.users import mock_user_data

# TODO: Add commentary on all the test cases


class UserServiceTestCase(TestCase):

    def setUp(self):
        ctx = test_app.test_request_context()
        ctx.push()
        self.service = UserService()
        self.user_schema = UserSchema()
        set_up_serializer()
        set_up_database()

    def tearDown(self):
        tear_down_database()

    def test_create_user(self):
        user_to_create = User(**mock_user_data)

        self.service.new_user(user_to_create)
        created_user = User.get(username=user_to_create.username)

        self.assertIs(created_user, user_to_create)


