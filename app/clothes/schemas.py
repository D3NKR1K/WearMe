from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

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

class SClothGet(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    brand: Brand = Field(..., description="Бренд одежды")
    category: Category = Field(..., description="Категория одежды")
    color: Color = Field(..., description="Цвет одежды")
    height: int = Field(..., description="Ростовая мерка одежды")
    chest: int = Field(..., description="...")
    waist: int = Field(..., description="...")
    hips: int = Field(..., description="...")

class SClothAdd(BaseModel):
    brand: Brand = Field(..., description="Бренд одежды")
    category: Category = Field(..., description="Категория одежды")
    color: Color = Field(..., description="Цвет одежды")
    height: int = Field(..., description="Ростовая мерка одежды")
    chest: int = Field(..., description="...")
    waist: int = Field(..., description="...")
    hips: int = Field(..., description="...")
