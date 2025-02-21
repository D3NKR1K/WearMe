from fastapi import FastAPI, HTTPException
from utils import *
import os
from typing import Optional, List

# Получает директорию текущего скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Переходит выше
parent_dir = os.path.dirname(script_dir)

# Получает путь к JSON пользователей
path_to_users_json = os.path.join(parent_dir, 'users.json')

# Получает путь к JSON одежды
path_to_clothing_json = os.path.join(parent_dir, 'clothing.json')

# Создает приложение
app = FastAPI()

# Возвращает название сайта
@app.get("/")
def home_page():
    return {"message": "WearMe",
            "description": "Приложение, которое позволяет вам подбирать одежду по вашим меркам"
            }

# Возвращает список всех пользователей
@app.get("/users")
def get_all_users() -> List[User]:
    return json_to_dict_list(path_to_users_json)

# Возвращает список всей одежды
@app.get("/clothing")
def get_all_cloth() -> List[Cloth]:
    return json_to_dict_list(path_to_clothing_json)

# Возвращает пользователя с указанным ID
@app.get("/user")
def get_user_from_param_id(user_id: int) -> User:
    users = json_to_dict_list(path_to_users_json)
    for user in users:
        if user["user_id"] == user_id:
            return user

@app.get("/cloth")
def get_cloth_from_param_id(cloth_id: int) -> Cloth:
    clothing = json_to_dict_list(path_to_clothing_json)
    for cloth in clothing:
        if cloth["clothing_id"] == cloth_id:
            return cloth

@app.post("/add_user")
def add_user_handler(user: User):
    user_dict = user.model_dump()
    check = add_user(user_dict)
    if check:
        return {"message": "Пользователь добавлен в базу данных"}
    else:
        return {"message": "Ошибка при добавлении пользователя"}

@app.put("/update_user")
def update_user_handler(filter_user: UserUpdateFilter, new_data: UserUpdate):
    check = upd_user(filter_user.model_dump(), new_data.model_dump())
    if check:
        return {"message": "Информация о мерках пользователя успешно обновлена"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при обновлении мерок пользователя")

@app.delete("/delete_user")
def delete_user_handler(filter_user: UserDeleteFilter):
    check = delete_user(filter_user.key, filter_user.value)
    if check:
        return {"message": "Пользователь успешно удален"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при удалении пользователя")