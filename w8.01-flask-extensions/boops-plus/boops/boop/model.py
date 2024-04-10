from sqlalchemy.sql import func
from boops.extensions import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer


class Boop(db.Model):
    """The Boop model."""

    __tablename__ = "boops"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement="auto")
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    pet_id = Column(Integer, ForeignKey("pets.id", ondelete="CASCADE"), nullable=False)
