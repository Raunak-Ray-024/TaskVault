from pydantic import BaseModel, ConfigDict

class UserSchema(BaseModel):
    name: str
    username: str
    password: str
    email: str
   
class UserResponseSchema(BaseModel):
    # # # Using ConfigDict is the type-safe way to handle configurations in V2
    # model_config = ConfigDict(from_attributes=True)
    model_config = ConfigDict(from_attributes=True)

    name: str
    username: str
    email: str
    id: int

    

class LoginSchema(BaseModel):
    username: str
    password: str
