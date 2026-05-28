from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime
from sqlalchemy import BigInteger, DateTime
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
