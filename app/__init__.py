from flask import Flask
from flask_injector import FlaskInjector
from app.database import Database, BaseModel
from sqlalchemy.orm import scoped_session
from app.serializer import Serializer

from config import bootstrap_configuration


class AppModule(Flask):

    def __init__(self, name=__name__):
        # Instantiate the WSGI application object
        super().__init__(name)
        self.config.from_object(bootstrap_configuration())

        self.database = Database(model_class=BaseModel)
        self.marshmallow = Serializer()
        self.injector = FlaskInjector(app=self, modules=AppModule.configure_binds)

    def initialize_modules(self):
        self.database.init_app(app=self)

        from app.users.models import User
        self.database.create_all(app=self)

        BaseModel.query = self.database.get_scoped_session().query_property()

        self.marshmallow.init_app(self)

        self.injector.map(session=self.database.create_scoped_session())


def configure_binds(binder):
    binder.bind(
        scoped_session,
        to=
    )


