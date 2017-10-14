#!env/bin/python
from app import app


class TestResource:

    @post
    def some_method(some_arg):
        return "Helloooo"


if __name__ == '__main__':
    app.run(debug=True, host='luxorv.local')
