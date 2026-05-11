# from fastapi import HTTPException,status,Request
# from src.user.dtos import UserSchema
# from sqlalchemy.orm import Session
# from src.user.modules import UserModel
# from pwdlib import PasswordHash
# from src.user.dtos import LoginSchema
# from src.utils.settings import settings
# from datetime import datetime,timedelta #time delta will help us to add minute
# import jwt
# from jwt.exceptions import InvalidTokenError


# # from passlib.context import CryptContext

# # pwd_context = CryptContext(
# #     schemes=["bcrypt"],
# #     deprecated="auto"
# # )

# # def get_password_hash(password):
# #     return pwd_context.hash(password)

# # def verify_password(plain_password, hashed_password):
# #     return pwd_context.verify(
# #         plain_password,
# #         hashed_password
# #     )



# def register(body:UserSchema,db:Session):
#     # print(body)
#     #username & email validation
#     is_user=db.query(UserModel).filter(UserModel.username==body.username).first()
#     if is_user:
#         raise HTTPException(400,detail="Username already exists")
#     is_email=db.query(UserModel).filter(UserModel.email==body.email).first()
#     if is_email:
#         raise HTTPException(400,detail="Email already exists")
    
#     hash_password=get_password_hash(body.password)
#     new_user=UserModel(
#         name=body.name,
#         username=body.username,
#         hash_password=hash_password,
#         email=body.email,
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# # def login_user(body:LoginSchema,db:Session):
# #     user=db.query(UserModel).filter(UserModel.username==body.username).first()
# #     if not user:
# #         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You entered wrong username")
# #     if not verify_password(body.password,user.hash_password):
# #         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You entered wrong username")
    
# #     exp_time=datetime.now()+timedelta(seconds=120)
# #     # print(exp_time)
# # #{} its the payload ek se xyada unique values ko pyaload mei decode kar sakte hai
# # #id toh same rahegi but exp time will change
# #     token=jwt.encode({"id":user.id,"exp":exp_time.timestamp()},settings.SECRET_KEY,settings.ALGORITHM)

# # #At this point where validation of username and password is done a token generation will be done by importing JWT       
# #     #its compulsory -id same to token same
# #     return {"token":token}


# def login_user(body: LoginSchema, db: Session):

#     user = db.query(UserModel).filter(
#         UserModel.username == body.username
#     ).first()

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid credentials"
#         )

#     if not verify_password(body.password, user.hash_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid credentials"
#         )

#     exp_time = datetime.utcnow() + timedelta(minutes=2)

#     token = jwt.encode(
#         {
#             "id": user.id,
#             "exp": exp_time
#         },
#         settings.SECRET_KEY,
#         algorithm=settings.ALGORITHM
#     )

#     return {"token": token}



# #TOKEN VALIDATION
# def is_authenticated(request:Request,db:Session):
#     try:
#         token=request.headers.get("authorization")
#         if not token:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are unauthorized")
#     # #jisne login kiya uska id dikh raha hai
#         token=token.split(" ")[-1]
#         data = jwt.decode(token, settings.SECRET_KEY,settings.ALGORITHM)
#         user_id=data.get("id")
#         exp_time=int(data.get("exp"))
#         current_time=datetime.now().timestamp()
#         print(exp_time-current_time)
#         if current_time>exp_time:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are unauthorized")
#         user=db.query(UserModel).filter(UserModel.id==user_id).first()
#         if not user:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are unnauthorized")
#         return user
#     except:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are unnauthorized")



from fastapi import HTTPException, status, Request,Depends
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.user.dtos import UserSchema, LoginSchema
from src.user.modules import UserModel
from src.utils.settings import settings


from datetime import datetime, timedelta

import jwt
from jwt.exceptions import InvalidTokenError

from passlib.context import CryptContext


# PASSWORD HASHING SETUP
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def get_password_hash(password):
    return pwd_context.hash(password[:72])


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# REGISTER USER
def register(body: UserSchema, db: Session):

    # USERNAME VALIDATION
    is_user = db.query(UserModel).filter(
        UserModel.username == body.username
    ).first()

    if is_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    # EMAIL VALIDATION
    is_email = db.query(UserModel).filter(
        UserModel.email == body.email
    ).first()

    if is_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    # PASSWORD HASHING
    hash_password = get_password_hash(body.password)

    # NEW USER
    new_user = UserModel(
        name=body.name,
        username=body.username,
        password=hash_password,
        email=body.email,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# LOGIN USER
def login_user(body: LoginSchema, db: Session):

    # FIND USER
    user = db.query(UserModel).filter(
        UserModel.username == body.username
    ).first()

    # USER NOT FOUND
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    # PASSWORD VERIFICATION
    if not verify_password(
        body.password,
        user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    # TOKEN EXPIRATION TIME
    exp_time = datetime.utcnow() + timedelta(minutes=2)

    # JWT TOKEN GENERATION
    token = jwt.encode(
        {
            "id": user.id,
            "exp": exp_time
        },
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return {
        "access_token": token
    }


from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def is_authenticated(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    try:

        token = credentials.credentials

        data = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        user_id = data.get("id")

        user = db.query(UserModel).filter(
            UserModel.id == user_id
        ).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )

        return user

    except InvalidTokenError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )