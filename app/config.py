"""
Модуль для работы с настройками приложения.
Использует pydantic для валидации и загрузки переменных окружения.
"""

import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Настройки базы данных
    DB_HOST: str = 'localhost'         # Хост PostgreSQL
    DB_PORT: int = 5432                # Порт PostgreSQL
    DB_NAME: str                       # Имя базы данных (обязательное)
    DB_USER: str                       # Пользователь БД (обязательное)
    DB_PASSWORD: str                   # Пароль пользователя (обязательное)

    # Настройки аутентификации JWT
    SECRET_KEY: str                    # Секретный ключ для подписи токенов
    ALGORITHM: str = 'HS256'           # Алгоритм подписи (по умолчанию HS256)

    # Конфигурация для загрузки переменных окружения
    model_config = SettingsConfigDict(
        # Путь к файлу .env относительно расположения этого файла
        env_file=os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..", ".env"
        ),
        env_file_encoding = 'utf-8',  # Кодировка файла .env
        case_sensitive = False  # Регистронезависимые переменные
    )

# Инициализация настроек при загрузке модуля
settings = Settings()

def get_db_url() -> str:
    """Формирует строку подключения к PostgreSQL."""
    return (
        f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}"
        f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    )

def get_auth_data() -> dict:
    """Возвращает данные для аутентификации."""
    return {
        "secret_key": settings.SECRET_KEY,
        "algorithm": settings.ALGORITHM
    }