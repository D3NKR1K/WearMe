from pydantic import ValidationError
from models import User, Cloth

def test_valid_user(data: dict) -> None:
    try:
        user = User(**data)
        print(user)
    except ValidationError as e:
        print(f"Ошибка валидации: {e}")

def test_valid_cloth(data: dict) -> None:
    try:
        cloth = Cloth(**data)
        print(cloth)
    except ValidationError as e:
        print(f"Ошибка валидации: {e}")

if __name__ == "__main__":
    user_data = {
    "user_id": 0,
    "name": "Роман",
    "email": "roman@example.com",
    "password": "123456789",
    "height": 176,
    "chest": 90,
    "waist": 50,
    "hips": 40
  }
    cloth_data = {
    "clothing_id": 0,
    "brand": "Ahuel",
    "category": "Ебал",
    "color": "Бирюзовый",
    "height": 176,
    "chest": 90,
    "waist": 50,
    "hips": 40
  }
    test_valid_user(user_data)
    test_valid_cloth(cloth_data)