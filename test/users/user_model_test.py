from app.users.models import User
from app import server

import unittest


class UserModelTestCase(unittest.TestCase):

    def setUp(self):
        server.db_session.commit()
        server.database.drop_all()
        server.database.create_all()
        self.user_data = dict(
            first_name='test',
            last_name='case',
            email='test@case.com',
            username='test_user',
            password='12345'
        )

    def tearDown(self):
        server.db_session.commit()
        server.database.drop_all()

    def test_creates_new_user(self):
        user_to_save: User = User(**self.user_data)
        user_to_save.save()

        created_user: User = User.get(username=user_to_save.username)

        self.assertEqual(created_user.id, user_to_save.id)
        self.assertEqual(created_user.first_name, user_to_save.first_name)
        self.assertEqual(created_user.last_name, user_to_save.last_name)
        self.assertEqual(created_user.email, user_to_save.email)
        self.assertEqual(created_user.username, user_to_save.username)
        self.assertEqual(created_user.password, user_to_save.password)

    def test_updates_user_info(self):
        user_to_update = User(**self.user_data)
        user_to_update.save()

        user_to_update.username = 'tesadfasf'
        user_to_update.update()

        updated_user = User.query.filter_by(id=1).first()

        self.assertEqual(updated_user.id, user_to_update.id)
        self.assertEqual(updated_user.first_name, user_to_update.first_name)
        self.assertEqual(updated_user.last_name, user_to_update.last_name)
        self.assertEqual(updated_user.email, user_to_update.email)
        self.assertEqual(updated_user.username, user_to_update.username)
        self.assertEqual(updated_user.password, user_to_update.password)
