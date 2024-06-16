from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import schemas
import database
import models


app = FastAPI()
@app.get("/")
async def root():
    return {"message":"Hello World"}


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

    for task in tasks:
        task_list.append(task)

    return task_list


@app.delete("/task/{id}")
def delete_task(task_id:int, db:Session=Depends(database.get_db)):
    task = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    db.delete(task)
    db.commit()


@app.patch("/task/{id}")
def update_task(id:int, task:schemas.UpdateTask, db:Session=Depends(database.get_db)):
    update_task = db.query(models.Tasks).get(id)
    update_task.title=task.title
    update_task.done=task.done
    update_task.deadline=task.deadline
    update_task.updated_at=datetime.now()
    db.commit()
