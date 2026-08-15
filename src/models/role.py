from sqlalchemy.orm import mapped_column, Mapped, relationship
import sqlalchemy as sa
from src.models.base import db
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.user import User

class Role(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String, nullable=False)
    user: Mapped[list['User']] = relationship('User', back_populates='role')
    
    def __repr__(self) -> str:
        return f"Role(id={self.id!r}, name={self.name!r})"
