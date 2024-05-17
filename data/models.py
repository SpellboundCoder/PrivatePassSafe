from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

db_url = "sqlite:///data/database.db"

engine = create_engine(db_url, echo=True)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(60))
    websites: Mapped[List["Website"]] = relationship(
        back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r}, password={self.password!r})"


class Website(Base):
    __tablename__ = "websites"
    id: Mapped[int] = mapped_column(primary_key=True)
    website: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(60))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="websites")

    def __repr__(self) -> str:
        return f"Website(id={self.id!r}, website={self.website!r}, email={self.email!r}, password={self.password})"


def create_database() -> None:
    return Base.metadata.create_all(engine)
