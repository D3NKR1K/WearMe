from pydantic import BaseModel, Field, EmailStr, ConfigDict


class SUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str = Field(..., min_length=1, max_length=50 ,description="Имя пользователя, от 1 до 50 символов")
    email: EmailStr = Field(..., description="Электронная почта пользователя")
    password: str = Field(..., min_length=8, max_length=32, description="Пароль пользователя, от 8 до 32 символов")
    height: int = Field(..., description="Рост пользователя")
    chest: int = Field(..., description="Мерка обхвата груди пользователя")
    waist: int = Field(..., description="Мерка обхвата талии пользователя")
    hips: int = Field(..., description="Мерка обхвата таза пользователя")