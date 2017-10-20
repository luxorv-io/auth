from flask import Flask
from app.users import users, models as user_models
from app.database import db, BaseModel
from app.serializer import ma, BaseSchema
from utils import import_all_subclasses_of

from config import bootstrap_configuration


class AppModule(Flask):

    def __init__(self, name=__name__):
        # Instantiate the WSGI application object
        super().__init__(name)
        self.config.from_object(bootstrap_configuration())
        self.db = db
        self.ma = ma        
        self.init_app()

    def init_app(self):
        self.register_blueprint(users)
        self.ma.app = self
        self.db.app = self
        self.ma.init_app(app=self)
        self.db.init_app(app=self)
        BaseModel.query = db.session.query_property()
        self.create_database()

    def create_database(self):
        import_all_subclasses_of(user_models, BaseModel, locals())

        if self.config  .get('testing'):
            self.db.drop_all(app=self)

        self.db.create_all(app=self)
