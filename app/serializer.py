from flask_marshmallow import Marshmallow

ma = Marshmallow()


class BaseSchema(ma.ModelSchema):
    pass
