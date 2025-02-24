from sqlalchemy.orm import Mapped
from app.database import Base, str_uniq, int_pk, int_null_true

# Модель таблицы пользователей
class User(Base):
    id: Mapped[int_pk]
    name: Mapped[str]
    email: Mapped[str_uniq]
    password: Mapped[str]
    height: Mapped[int]
    chest: Mapped[int]
    waist: Mapped[int]
    hips: Mapped[int]

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"name={self.name!r}")

    def __repr__(self):
        return str(self)