from flask import Flask
from app.database import Database, BaseModel
from app.serializer import Serializer

from config import bootstrap_configuration


class AppModule(Flask):

    def __init__(self, name):
        # Instantiate the WSGI application object
        super().__init__(name)
        self.config.from_object(bootstrap_configuration())

        self.database = Database(model_class=BaseModel)
        self.database.init_app(self)
        self.db_session = self.database.create_scoped_session()

        self.marshmallow = Serializer()
        self.marshmallow.init_app(self)


server = AppModule(__name__)

