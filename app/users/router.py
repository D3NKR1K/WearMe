from fastapi import APIRouter
from app.users.dao import UserDAO
from app.users.schemas import SUserGet, SUserAdd, SUserUpdateMeasure

router = APIRouter(prefix='/users', tags=['Работа с пользователями'])

@router.get("/", summary="Получить всех пользователей", response_model=list[SUserGet])
async def get_all_users():
    return await UserDAO.find_all()

@router.post("/register/", summary="Регистрация нового пользователя")
async def register_user(user: SUserAdd) -> dict:
    check = await UserDAO.add(**user.model_dump())
    if check:
        return {"message": "Пользователь успешно зарегистрирован!"}
    else:
        return {"message": "Ошибка при регистрации пользователя!"}

@router.put("/update_measurements/", summary="Обновление мерок пользователя")
async def update_user_measurements(user: SUserUpdateMeasure) -> dict:
    check = await UserDAO.update(filter_by = {'email' : user.email},
                                 height = user.height,
                                 chest = user.chest,
                                 waist = user.waist,
                                 hips = user.hips)
    if check:
        return {"message" : "Мерки пользователя успешно обновлены!"}
    else:
        return {"message" : "Ошибка при обновлении мерок пользователя!"}

@router.delete("/delete/{user_id}", summary="Удаление пользователя")
async def delete_user(user_id: int) -> dict:
    check = await UserDAO.delete(id = user_id)
    if check:
        return {"message" : f"Пользователь с ID {user_id} успешно удален!"}
    else:
        return {"message" : "Ошибка при удалении пользователя"}