from fastapi import APIRouter, Depends, status, Request,HTTPException,Security
from sqlalchemy.orm import Session
from src.user.dtos import UserSchema, UserResponseSchema, LoginSchema
from src.utils.db import get_db
from src.user import controller
from fastapi.security import HTTPBearer
from src.utils.helpers import is_authenticated
from src.user.modules import UserModel



security = HTTPBearer()

user_router=APIRouter(prefix="/user")

@user_router.post("/register",response_model=UserResponseSchema,status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session=Depends(get_db)):
    return controller.register(body,db)

# @user_router.post("/login",status_code=status.HTTP_200_OK)
# def login(body:LoginSchema,db:Session=Depends(get_db)):
#     return controller.login_user(body,db)


from fastapi import Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

@user_router.post("/login", status_code=status.HTTP_200_OK)
def login(body: LoginSchema, db: Session = Depends(get_db)):

    user = controller.login_user(body, db)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # If controller already returns token
    if isinstance(user, dict) and "access_token" in user:

        return JSONResponse(
            status_code=200,
            content={
                "access_token": user["access_token"],
                "token_type": "bearer"
            }
        )

    # If controller returns raw token string
    if isinstance(user, str):

        return JSONResponse(
            status_code=200,
            content={
                "access_token": user,
                "token_type": "bearer"
            }
        )

    raise HTTPException(
        status_code=500,
        detail="Login response invalid"
    )

# @user_router.get("/is_auth",status_code=status.HTTP_200_OK,response_model=UserResponseSchema)
# def is_auth(request:Request,db:Session=Depends(get_db), credentials=Security(security) ):
#     return controller.is_authenticated(request,db)

@user_router.get("/is_auth", status_code=status.HTTP_200_OK, response_model=UserResponseSchema)
def is_auth(user: UserModel = Depends(is_authenticated)):
    return user

