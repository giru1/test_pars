import uuid

from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from database import Base


class Film(Base):
    """
    Модель фильма

    Атрибуты
    --------

    id : int
        идентификатор
    name : str
        наименование
    producer: str
        режисер
    year : str
        год
    genre : str
        жанр
    rating : str
        рейтинг
    """

    __tablename__ = "film"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    name: Mapped[str] = mapped_column(nullable=True)
    image_path: Mapped[str] = mapped_column(nullable=True)
    producer: Mapped[str] = mapped_column(nullable=True)
    year: Mapped[int] = mapped_column(nullable=True)
    genre: Mapped[str] = mapped_column(nullable=True)
    rating: Mapped[float] = mapped_column(nullable=True)
