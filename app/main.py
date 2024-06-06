from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import schemas, database, models

app = FastAPI()
# @app.get("/")
# async def root():
#     return {"message":"Hello World"}


@app.post("/tasks")
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    task = models.Tasks(
        title=task.title,
        done=False,
        deadline=task.deadline,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return task


@app.get("/tasks")
def get_tasks(db: Session=Depends(database.get_db)):
    task_list = []
    tasks = db.query(models.Tasks).all()
    print(tasks)

    for task in tasks:
        task_list.append(task)

    return task_list
# app.include_router(tasks.router)
# app.include_router(users.router)
