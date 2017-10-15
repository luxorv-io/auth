from flask import Flask
from injector import Module, provider
from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import scoped_session


class Database(Module):

    @provider
    def provide_ext(self, app: Flask) -> scoped_session:
        return



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

