from sqlalchemy import Column, Integer, DateTime, func
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel(Base):
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


db = SQLAlchemy(model_class=BaseModel)