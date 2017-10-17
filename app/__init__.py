from flask import Flask
from app.users import users, models as user_models
from app.database import db, BaseModel
from utils import import_all_subclasses_of

from config import bootstrap_configuration


class AppModule(Flask):

    def __init__(self, name=__name__):
        # Instantiate the WSGI application object
        super().__init__(name)
        self.config.from_object(bootstrap_configuration())
        self.db = db
        self.init_app()

    def init_app(self):
        self.register_blueprint(users)
        self.db.init_app(app=self)
        self.create_database()

    def create_database(self):
        import_all_subclasses_of(user_models, BaseModel, locals())
        self.db.create_all(app=self)