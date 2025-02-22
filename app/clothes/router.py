from fastapi import APIRouter, Depends
from app.clothes.dao import ClothDAO
from app.clothes.rb import RBCloth
from app.clothes.schemas import SCloth

router = APIRouter(prefix='/clothes', tags=['Работа с одеждой'])

@router.get("/", summary="Получить всю одежду")
async def get_all_users(request_body: RBCloth = Depends()) -> list[SCloth]:
    return await ClothDAO.find_all(**request_body.to_dict())