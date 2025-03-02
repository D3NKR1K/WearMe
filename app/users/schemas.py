"""
Модуль с Pydantic-схемами для валидации данных и сериализации.
Определяет структуру запросов и ответов API.
"""

from typing import Optional
from pydantic import BaseModel, Field, EmailStr, ConfigDict


class SUserGet(BaseModel):
    """
    Схема для получения данных пользователя.
    Используется в ответах API, исключает чувствительные данные.
    """

    model_config = ConfigDict(
        from_attributes=True,  # Разрешает парсинг из ORM-объектов
        json_schema_extra={
            "example": {
                "name": "Иван Иванов",
                "email": "user@example.com",
                "height": 180,
                "chest": 95,
                "waist": 80,
                "hips": 100
            }
        }
    )

    name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Полное имя пользователя (1-50 символов)"
    )

    email: EmailStr = Field(
        ...,
        description="Валидный email адрес"
    )

    height: Optional[int] = Field(
        None,
        ge=50,
        le=250,
        description="Рост в сантиметрах (50-250 см)",
        examples=[170, 180]
    )

    chest: Optional[int] = Field(
        None,
        ge=50,
        le=200,
        description="Обхват груди в см (50-200 см)"
    )

    waist: Optional[int] = Field(
        None,
        ge=50,
        le=200,
        description="Обхват талии в см (50-200 см)"
    )

    hips: Optional[int] = Field(
        None,
        ge=50,
        le=200,
        description="Обхват бедер в см (50-200 см)"
    )

class SUserRegister(BaseModel):
    """
    Схема для регистрации нового пользователя.
    """

    name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Полное имя пользователя (1-50 символов)",
        examples=["Алексей Петров"]
    )

    email: EmailStr = Field(
        ...,
        description="Валидный email для входа в систему",
        examples=["user@example.com"]
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=32,
        description="Пароль (8-32 символа, минимум 1 цифра и заглавный символ)",
        examples=["SecurePass123!"]
    )

class SUserUpdateMeasure(BaseModel):
    """
        Схема для обновления антропометрических данных.
        Все поля опциональны для частичного обновления.
        """
    email: EmailStr = Field(
        ...,
        description="Email пользователя для идентификации"
    )

    height: Optional[int] = Field(
        None,
        ge=50,
        le=250,
        description="Новый рост в см"
    )

    chest: Optional[int] = Field(
        None,
        ge=50,
        le=200,
        description="Новый обхват груди"
    )

    waist: Optional[int] = Field(
        None,
        ge=50,
        le=200,
        description="Новый обхват талии"
    )

    hips: Optional[int] = Field(
        None,
        ge=50,
        le=200,
        description="Новый обхват бедер"
    )

class SUserAuth(BaseModel):
    """
        Схема для аутентификации пользователя.
        Используется при входе в систему.
        """
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "user@example.com",
                "password": "SecurePass123!"
            }
        }
    )

    email: EmailStr = Field(
        ...,
        description="Email, указанный при регистрации"
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=32,
        description="Пароль учетной записи"
    )