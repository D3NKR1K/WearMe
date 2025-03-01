from fastapi import FastAPI
from app.users.router import router as router_users
from app.clothes.router import router as router_clothes


app = FastAPI()

app.include_router(router_users)
app.include_router(router_clothes)