#!env/bin/python
from app import AppModule
from app import users

server = AppModule()

if __name__ == '__main__':
    server.run(
        debug=True,
        host='luxorv.io'
    )
