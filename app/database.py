from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import Column, Integer, DateTime, func


class Database(SQLAlchemy):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BaseModel(object):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    date_created = Column(
        DateTime,
        default=func.current_timestamp()
    )
    date_modified = Column(
        DateTime,
        default=func.current_timestamp(),
        onupdate=func.current_timestamp()
    )
