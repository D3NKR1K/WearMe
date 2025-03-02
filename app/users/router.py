from fastapi import APIRouter, HTTPException, status
from app.users.dao import UserDAO
from app.users.auth import get_password_hash, authenticate_user
from app.users.schemas import *

router = APIRouter(prefix='/users', tags=['Работа с пользователями'])


@router.post("/register/", summary="Регистрация нового пользователя")
async def register_user(user_data: SUserRegister) -> dict:
    user = await UserDAO.find_one_or_none_by_email(user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.model_dump()
    user_dict['password'] = get_password_hash(user_data.password)
    await UserDAO.add(**user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}


@router.post("/login/", summary="Авторизация пользователя")
async def auth_user(user_data: SUserAuth):
    check = await authenticate_user(email=user_data.email, password=user_data.password)
    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Неверная почта или пароль")
    return {'message': "Вы успешно авторизованы!"}
