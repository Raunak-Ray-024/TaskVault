from fastapi import APIRouter,Depends,status  #Depends Dependency injection system
from src.task import controller  #controller contains crud functions
from src.task.dtos import TaskSchema,TaskResponseSchema #requeest validation schema Pydantic
from src.utils.db import get_db  #provides DB session per request 
from typing import List
from sqlalchemy.orm import Session
from src.utils.helpers import is_authenticated
from src.user.modules import UserModel

task_routes=APIRouter(prefix="/tasks")
@task_routes.post("/create")
def create_task(
    body: TaskSchema,
    db: Session = Depends(get_db),
    user: UserModel = Depends(is_authenticated)
):
    return controller.create_task(body, db, user)

#jab bhi hamara code successfully create hoga it'll show status code 201
#ResponseSchema jab hum koi bhi extra value add karenge toh woh add nhi hoga by response model
# @task_routes.post("/create",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
# #first parameter-Validates incoming JSON using schema 
# #second param- injects DB sessions calls get_db function , provides fresh session for request
# def create_task(body:TaskSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):  
#     return controller.create_task(body,db,user)

@task_routes.get("/all_tasks",response_model=List[TaskResponseSchema],status_code=status.HTTP_200_OK)
def get_all_tasks(body:TaskSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.get_tasks(db,user)  #applying list we will get list of all task response schema

@task_routes.get("/get_one_task/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_200_OK)
def get_one_task(task_id:int,body:TaskSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.get_one_task(task_id,db)

@task_routes.put("/update_task/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def update_task(body:TaskSchema,task_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.update_task(body,task_id,db,user)

@task_routes.delete("/delete_task/{task_id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,body:TaskSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.delete_task(task_id,db)