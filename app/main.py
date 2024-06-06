from fastapi import FastAPI, Depends
from routers import tasks, users
from sqlalchemy.orm import Session
import schemas, database, models

app = FastAPI()
# @app.get("/")
# async def root():
#     return {"message":"Hello World"}

@app.post("/tasks")
def create_task( task:schemas.TaskCreate, db:Session=Depends(database.get_db)):
    task = models.Tasks(
        title = task.title,
        done = False,
        deadline = task.deadline,
        created_at = datetime.now,
        updated_at = datatime.now
    )
    db.add(task)
    db.commit()
    db.refresh(task)

# app.include_router(tasks.router)
# app.include_router(users.router)
