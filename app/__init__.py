from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import bootstrap_configuration

# Start the configuration bootstrap
selected_config = bootstrap_configuration()

# Instantiate the WSGI application object
app = Flask(__name__)

# Configure the app
app.config.from_object(selected_config)

# Define db object to be used by other modules
db = SQLAlchemy(app)

# TODO db create all