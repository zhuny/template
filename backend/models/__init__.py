from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import Column, Integer, DateTime, func


class BaseModel(Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    created_at = Column(DateTime, default=func.now(), server_default="now()")
    updated_at = Column(
        DateTime,
        default=func.now(), server_default="now()",
        onupdate=func.now(), server_onupdate="now()"
    )


db = SQLAlchemy(model_class=BaseModel)
migrate = Migrate(db=db)


def init(app: Flask):
    db.init_app(app)
    migrate.init_app(app)
