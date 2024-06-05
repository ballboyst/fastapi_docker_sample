from fastapi import FastAPI
from routers import tasks, users
from database import engine, Sessionlocal


app = FastAPI()
# @app.get("/")
# async def root():
#     return {"message":"Hello World"}


app.include_router(tasks.router)
app.include_router(users.router)
