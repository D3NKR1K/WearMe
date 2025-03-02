"""
Модуль для работы с базой данных.
Содержит настройки подключения, базовую модель и аннотации для типов колонок.
"""


from datetime import datetime
from typing import Annotated, Any, AsyncGenerator
from sqlalchemy import func, Text
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncAttrs,
    AsyncSession
)
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from app.config import get_db_url

# Получаем строку подключения из конфига
DATABASE_URL = get_db_url()

# Создаем асинхронный движок с настройками пула соединений
engine = create_async_engine(
    DATABASE_URL,
    pool_size=20,          # Максимальное число соединений в пуле
    max_overflow=10,       # Максимальное число соединений сверх pool_size
    pool_pre_ping=True     # Проверка активности соединений перед использованием
)

# Фабрика асинхронных сессий с настройками
async_session_maker = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,  # Не сбрасывать состояние объектов после коммита
    class_=AsyncSession,
    autoflush=False          # Отключаем автоочистку для лучшего контроля
)

# Настройка аннотаций
# Аннотации для часто используемых типов колонок
int_pk = Annotated[
    int,
    mapped_column(primary_key=True, comment="Первичный ключ")
]

created_at = Annotated[
    datetime,
    mapped_column(
        server_default=func.now(),
        comment="Дата и время создания записи"
    )
]

updated_at = Annotated[
    datetime,
    mapped_column(
        server_default=func.now(),
        onupdate=func.now(),  # Для автообновления при изменении записи
        comment="Дата и время последнего обновления"
    )
]

str_uniq = Annotated[
    str,
    mapped_column(
        Text,
        unique=True,
        index=True,
        nullable=False,
        comment="Уникальная строка с индексом"
    )
]

int_nullable = Annotated[
    int,
    mapped_column(
        nullable=True,
        comment="Целое число, допускающее NULL"
    )
]

class Base(AsyncAttrs, DeclarativeBase):
    """
    Базовый класс для всех моделей SQLAlchemy.
    Автоматически генерирует имя таблицы и добавляет временные метки.
    """

    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """
        Генерирует имя таблицы из имени класса
        """
        return f"{cls.__name__.lower()}s"

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

async def get_async_session() -> AsyncGenerator[AsyncSession | Any, Any]:
    """
    Генератор асинхронных сессий для использования в Dependency Injection.
    Гарантирует закрытие сессии даже при возникновении ошибок.
    """
    async with async_session_maker() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise
        finally:
            await session.close()