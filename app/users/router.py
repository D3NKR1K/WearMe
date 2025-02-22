from fastapi import APIRouter
from app.users.dao import UserDAO
from app.users.schemas import SUser

router = APIRouter(prefix='/users', tags=['Работа с пользователями'])

@router.get("/", summary="Получить всех пользователей", response_model=list[SUser])
async def get_all_users():
    return await UserDAO.find_all()