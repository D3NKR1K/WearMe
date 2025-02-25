from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
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

    is_user: Mapped[bool] = mapped_column(default=True, server_default=text('true'), nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)
    is_super_admin: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)

    extend_existing = True

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"name={self.name!r}")

    def __repr__(self):
        return str(self)