from fastapi import FastAPI
from routers import tasks


app = FastAPI()
# @app.get("/")
# async def root():
#     return {"message":"Hello World"}


app.include_router(tasks.router)

