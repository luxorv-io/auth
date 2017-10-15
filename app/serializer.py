from flask_marshmallow import Marshmallow
from flask_marshmallow import sqla


class Serializer(Marshmallow):

    def __init__(self):
        super(Serializer).__init__()
        self.ModelSchema = sqla.ModelSchema
