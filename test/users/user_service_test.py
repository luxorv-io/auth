from app.users.services import UserService
from test import set_up_database, tear_down_database
from unittest import TestCase


class UserServiceTest(TestCase):

    def setUp(self):
        self.service = UserService()
        set_up_database()

    def tearDown(self):
        tear_down_database()

    def test_get_user_by_field(self):
        pass


