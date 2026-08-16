import sqlalchemy as sa
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .base import db


class User(db.Model):    
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)    
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)    
    password: Mapped[str] = mapped_column(sa.String, nullable=False)    
    active: Mapped[bool] = mapped_column(sa.Boolean, default=True)    
    role_id: Mapped[int] = mapped_column(sa.ForeignKey('role.id'), nullable=True)    
    role: Mapped['Role'] = relationship('Role', back_populates='user')

    def __repr__(self) -> str:       
        return f"User(id={self.id!r}, username={self.username!r}, active={self.active!r}))"
