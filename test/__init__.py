import unittest
from app import AppModule


test_app = AppModule(__name__)

from test import users

if __name__ == '__main__':
    unittest.main()
