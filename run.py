#!env/bin/python
from app import app
from app import users

if __name__ == '__main__':
    app.run(debug=True, host='luxorv.io')
