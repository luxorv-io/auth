from app import app

import unittest


class UserIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_loads_all_users(self):
        client = app.test_client()
