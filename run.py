#!env/bin/python
from app import server
from app import users

if __name__ == '__main__':
    server.run(
        debug=True,
        host='luxorv.io'
    )
