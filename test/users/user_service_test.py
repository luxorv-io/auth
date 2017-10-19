from unittest import TestCase
from mockito import when, verify, when2, expect
from app.users.services import UserService
from app.users.models import User

from app.users.models.responses import UserSchema

from flask import jsonify

from test.users import mock_user_data
from test import set_up_database, tear_down_database, set_up_serializer

import json

class UserServiceTest(TestCase):

    def setUp(self):
        self.service = UserService()
        self.user_schema = UserSchema()
        set_up_serializer()
        set_up_database()

    def tearDown(self):
        tear_down_database()

    def test_create_user(self):
        user_to_create = User(**mock_user_data)
        user_json = self.user_schema.dump(user_to_create).data

        when(jsonify)\
            .__call__(user_json)\
            .thenReturn(json.dumps(mock_user_data))

        self.service.new_user(user_to_create)

        created_user = User.get(username=user_to_create.username)

    def test_get_user_by_field(self):
        pass


