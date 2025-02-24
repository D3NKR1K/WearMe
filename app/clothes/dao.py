from app.dao.base import BaseDAO
from app.clothes.models import Cloth


class ClothDAO(BaseDAO):
    model = Cloth