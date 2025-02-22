from fastapi import FastAPI
from app.users.router import router as router_users
from app.clothes.router import router as router_clothes


app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "WearMe",
            "description": "Приложение, которое позволяет вам подобрать одежду по вашим индивидуальным меркам"}

app.include_router(router_users)
app.include_router(router_clothes)