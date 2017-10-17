import unittest
from test import users
from app import AppModule


test_app = AppModule(__name__)


if __name__ == '__main__':
    unittest.main()