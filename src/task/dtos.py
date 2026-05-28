from pydantic import BaseModel
from typing import Optional

class TaskSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


class TaskResponseSchema(BaseModel):
    id:Optional[int]
    title: Optional[str] 
    description: Optional[str] 
    is_completed: Optional[bool] 
    user_id:int|None = 0
    model_config = {  #data ko object form mei bhi accept kar sakta hai
    "from_attributes": True
    } 