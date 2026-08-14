from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from datetime import datetime



class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


class Role(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String, nullable=False)
    user: Mapped[list['User']] = relationship('User', back_populates='role')
   
    def __repr__(self) -> str:
        return f"Role(id={self.id!r}, name={self.name!r})"


class User(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(sa.String, nullable=False)
    active: Mapped[bool] = mapped_column(sa.Boolean, default=True)
    role_id: Mapped[int] = mapped_column(sa.ForeignKey('role.id'), nullable=True)
    role: Mapped['Role'] = relationship('Role', back_populates='user')

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, active={self.active!r})"


class Post(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(sa.String, nullable=False)
    body: Mapped[str] = mapped_column(sa.String, nullable=False)
    created: Mapped[datetime] = mapped_column(sa.DateTime, server_default=sa.func.now())
    author_id: Mapped[int] = mapped_column(sa.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, title={self.title!r}, author_id={self.author_id!r})"