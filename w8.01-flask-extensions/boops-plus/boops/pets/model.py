from typing import List
from sqlalchemy.sql import func
from boops.extensions import db
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String


class Pet(db.Model):
    """The Pet model."""

    __tablename__ = "pets"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(45), nullable=False)
    type = Column(String(45), nullable=False)
    birthday = Column(Date, nullable=False)
    is_derpy = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    boops = relationship("Boop", backref="pet", cascade="all, delete")

    def has_been_booped_by(self, user_id):
        """Returns True if user booped pet, else False."""

        has_booped = False
        for boop in self.boops:
            if boop.user_id == user_id:
                has_booped = True
        return has_booped
