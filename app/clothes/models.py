from sqlalchemy.orm import Mapped
from app.database import Base, int_pk

# Модель таблицы одежды
class Cloth(Base):
    id: Mapped[int_pk]
    brand: Mapped[str]
    category: Mapped[str]
    color: Mapped[str]
    height: Mapped[int]
    chest: Mapped[int]
    waist: Mapped[int]
    hips: Mapped[int]

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, brand={self.brand!r}, color={self.color!r}, category={self.category!r})"

    def __repr__(self):
        return str(self)