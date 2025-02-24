from fastapi import APIRouter, Depends
from app.clothes.dao import ClothDAO
from app.clothes.rb import RBCloth
from app.clothes.schemas import SClothGet, SClothAdd

router = APIRouter(prefix='/clothes', tags=['Работа с одеждой'])

@router.get("/", summary="Получить всю одежду c(без) фильтрами(ов)")
async def get_all_clothes(request_body: RBCloth = Depends()) -> list[SClothGet]:
    return await ClothDAO.find_all(**request_body.to_dict())

@router.get("/{cloth_id}", summary="Получить единицу одежды по ID")
async def get_cloth_by_id(cloth_id: int) -> SClothGet | dict:
    result = await ClothDAO.find_one_or_none_by_id(cloth_id)
    if result is None:
        return {"message": f"Одежда с ID {cloth_id} не найдена!"}
    return result

@router.post("/add/", summary="Добавление одежды в БД")
async def register_user(user: SClothAdd) -> dict:
    check = await ClothDAO.add(**user.model_dump())
    if check:
        return {"message": "Элемент одежды успешно добавлен!"}
    else:
        return {"message": "Ошибка при добавлении элемента одежды!"}