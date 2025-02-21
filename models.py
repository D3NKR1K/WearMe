from enum import Enum
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Any

class Brand(str, Enum):
    guci = "Guci"
    pima = "Pima"
    noke = "Noke"
    abibas = "Abibas"

class Category(str, Enum):
    tshirt = "Футболка"
    shirt = "Рубашка"
    pants = "Брюки"
    shorts = "Шорты"

class Color(str, Enum):
    black = "Черный"
    red = "Красный"
    blue = "Синий"
    green = "Зеленый"
    white = "Белый"

class User(BaseModel):
    user_id: int
    name: str = Field(default=..., min_length=1, max_length=50, description="Имя пользователя, от 1 до 50 символов")
    email: EmailStr = Field(default=..., description="Электронная почта пользователя")
    password: str = Field(default=..., min_length=8, max_length=32, description="Пароль пользователя, от 8 до 32 символов")
    height: int = Field(default=..., description="Рост пользователя")
    chest: int = Field(default=..., description="...")
    waist: int = Field(default=..., description="...")
    hips: int = Field(default=..., description="...")

class Cloth(BaseModel):
    clothing_id: int
    brand: Brand = Field(default=..., description="Бренд одежды")
    category: Category = Field(default=..., description="Категория одежды")
    color: Color = Field(default=..., description="Цвет одежды")
    height: int = Field(default=..., description="Ростовая мерка одежды")
    chest: int = Field(default=..., description="...")
    waist: int = Field(default=..., description="...")
    hips: int = Field(default=..., description="...")

class UserUpdateFilter(BaseModel):
    user_id: int

class UserUpdate(BaseModel):
    height: int = Field(default=..., description="Ростовая мерка одежды")
    chest: int = Field(default=..., description="...")
    waist: int = Field(default=..., description="...")
    hips: int = Field(default=..., description="...")

class UserDeleteFilter(BaseModel):
    key: str
    value: Any