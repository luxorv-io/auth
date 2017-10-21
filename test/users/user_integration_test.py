from test import test_app, set_up_database
from test.users import mock_user_data

from app.users.models import User
from app.users.models.responses import UserSchema
from app.users.services import UserService

from unittest import TestCase

import json


class UserIntegrationTestCase(TestCase):
    def setUp(self):
        ctx = test_app.app_context()
        ctx.push()

        ctx = test_app.test_request_context()
        ctx.push()

        set_up_database()

        self.client = test_app.test_client()
        self.service = UserService()
        self.user_schema = UserSchema()

    def test_loads_all_users(self):
        self.add_new_user()
        self.add_new_user()
        self.add_new_user()

        response = self.client.get("/users")
        users_json = json.loads(response.data)

        self.assertIs(len(users_json), 3)
        self.assertIs(response.status_code, 200)

    def test_creates_new_user(self):
        user_to_create = User(**mock_user_data)

        response = self.client.post(
            "/users",
            data=json.dumps(mock_user_data),
            content_type='application/json'
        )

        created_user = User(**json.loads(response.data))

        self.assertIs(response.status_code, 200)
        self.assertEqual(user_to_create.username, created_user.username)
        self.assertEqual(user_to_create.first_name, created_user.first_name)
        self.assertEqual(user_to_create.last_name, created_user.last_name)
        self.assertEqual(user_to_create.email, created_user.email)

    def add_new_user(self):
        self.service.new_user(User(**mock_user_data))


