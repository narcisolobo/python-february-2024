from flask_login import UserMixin
from sqlalchemy import DATETIME, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from boops.extensions import db


class User(UserMixin, db.Model):
    """The User model."""

    __tablename__ = "users"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement="auto")
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(60), nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=func.now())
    updated_at = Column(DATETIME, onupdate=func.now())
    pets = relationship("Pet", backref="owner", cascade="all, delete")
    boops = relationship("Boop", backref="user", cascade="all, delete")
