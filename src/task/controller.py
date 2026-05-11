from src.task.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.task.modules import TaskModel  #ORM model (represents DB table)
from fastapi import HTTPException
from src.user.modules import UserModel




def create_task(body:TaskSchema,db:Session,user:UserModel):
    data=body.model_dump()  #convert schema to dictionary
    new_task=TaskModel(title=data["title"],description=data["description"], is_completed=data["is_completed"],user_id=user.id) #create ORM object

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task  #for al def new_task is a list of object  for task model

def get_tasks(db:Session,user:UserModel):
    tasks=db.query(TaskModel).filter(TaskModel.user_id==user.id).all()
    # return{"status":"All tasks","data":tasks}
    return tasks  

def get_one_task(task_id:int,db:Session):
    one_Task=db.query(TaskModel).get(task_id)
    if not one_Task:
        return HTTPException(404,detail="task_id is incorrect")
    # return{"status":"found","data":one_Task}
    return one_Task

def update_task(body:TaskSchema,task_id:int,db:Session,user:UserModel):
    one_Task:TaskModel=db.query(TaskModel).get(task_id)
    if not one_Task:
        return HTTPException(status_code=404,detail="task_id is incorrect")
    if one_Task.user_id!=user.id:
        return HTTPException(status_code=401,detail="you are not allowed")

    # one_Task.title=body.title
    # one_Task.description=body.description
    # one_Task.is_completed=body.is_completed

    body=body.model_dump(exclude_unset=True)
    for field,value in body.items():
        setattr(one_Task,field,value)

    db.add(one_Task)
    db.commit()
    db.refresh(one_Task)
    return one_Task
    # return{"status":"task updated","data":one_Task}   

def delete_task(task_id:int,db:Session):
    one_Task=db.query(TaskModel).get(task_id)
    if not one_Task:
        return HTTPException(status_code=404,detail="task_id is incorrect")
    db.delete(one_Task)
    db.commit()

    return {"status":"task deleted"}  
