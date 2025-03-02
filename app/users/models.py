"""
Модели данных SQLAlchemy.
Определяет структуру таблиц и бизнес-логику сущностей.
"""

from sqlalchemy import Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base, str_uniq, int_pk, int_nullable


# Модель таблицы пользователей
class User(Base):
    """
    Модель пользователя системы.

    Атрибуты:
    - id: уникальный идентификатор
    - name: полное имя пользователя
    - email: уникальный email (логин)
    - password: хеш пароля
    - body_measurements: антропометрические данные
    - ролевые флаги: is_user, is_admin, is_super_admin
    """

    __tablename__ = "users"

    # Базовые поля
    id: Mapped[int_pk] = mapped_column(comment="Уникальный идентификатор пользователя")
    name: Mapped[str] = mapped_column(Text, comment="Полное имя пользователя")
    email: Mapped[str_uniq] = mapped_column(comment="Уникальный email для входа")
    password: Mapped[str] = mapped_column(Text, comment="Хеш пароля (BCrypt)")

    # Антропометрические данные (опциональные)
    height: Mapped[int_nullable] = mapped_column(
        comment="Рост в сантиметрах (необязательно)")
    chest: Mapped[int_nullable] = mapped_column(
        comment="Обхват груди в см (необязательно)")
    waist: Mapped[int_nullable] = mapped_column(
        comment="Обхват талии в см (необязательно)")
    hips: Mapped[int_nullable] = mapped_column(
        comment="Обхват бедер в см (необязательно)")

    # Ролевые флаги
    is_user: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        server_default="true",
        nullable=False,
        comment="Флаг обычного пользователя"
    )

    is_admin: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default="false",
        nullable=False,
        comment="Флаг администратора"
    )

    is_super_admin: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default="false",
        nullable=False,
        comment="Флаг супер-администратора"
    )

    def __str__(self):
        return (
            f"User(id={self.id}, "
            f"email={self.email}, "
            f"roles={self.get_roles()})"
        )

    def __repr__(self):
        return f"<{self.__str__()}>"

    def get_roles(self) -> list[str]:
        """Возвращает список ролей пользователя."""
        roles = []
        if self.is_super_admin:
            roles.append("super_admin")
        elif self.is_admin:
            roles.append("admin")
        if self.is_user:
            roles.append("user")
        return roles
