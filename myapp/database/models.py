from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime
from sqlalchemy import BigInteger, Date, Integer, func, ForeignKey, Time, DateTime
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


# Таблица Пользователей
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now())


# Таблица Услуг
class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    duration: Mapped[int] = mapped_column(Integer)
    price: Mapped[int] = mapped_column(Integer)


# Таблица Записей
class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    service_id: Mapped[int] = mapped_column(Integer, ForeignKey("services.id"))
    booking_date: Mapped[datetime] = mapped_column(Date)
    booking_time: Mapped[datetime] = mapped_column(Time)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                server_default=func.now()
    )
