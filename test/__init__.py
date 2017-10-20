from unittest import TestSuite, defaultTestLoader, TextTestRunner
from app import AppModule
from app.database import db
from app.serializer import ma

test_modules = [
    'test.users.user_integration_test',
    'test.users.user_model_test',
    'test.users.user_service_test',
]

test_app = AppModule()


def start_suite():
    # Establish an application context before running the tests.
    test_suite = TestSuite()
    test_runner = TextTestRunner()

    for mod in test_modules:
        test_suite.addTest(defaultTestLoader.loadTestsFromName(mod))

    test_runner.run(test_suite)


def set_up_database():
    ctx = test_app.app_context()
    ctx.push()

    db.session.commit()
    db.drop_all(app=test_app)
    db.create_all(app=test_app)


def set_up_serializer():
    ma.init_app(app=test_app)


def tear_down_database():
    db.session.commit()
    db.drop_all()


if __name__ == '__main__':
    start_suite()
