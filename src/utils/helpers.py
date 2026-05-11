# from fastapi import Request,HTTPException,status,Depends
# from src.utils.settings import settings
# from sqlalchemy.orm import Session
# from jwt.exceptions import InvalidTokenError
# from src.user.modules import UserModel
# import jwt
# from datetime import datetime,timedelta
# from src.utils.db import get_db





# def is_authenticated(request:Request,db:Session=Depends(get_db)):
#     try:
#         token=request.headers.get("authorization")
#         if not token:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are unauthorized")
#     # #jisne login kiya uska id dikh raha hai
#         token=token.split(" ")[-1]
#         data = jwt.decode(token, settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
#         user_id=data.get("id")
#         # exp_time=int(data.get("exp"))
#         # current_time=datetime.now().timestamp()
#         # print(exp_time-current_time)
#         # if current_time>exp_time:
#         #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are unauthorized")
#         user=db.query(UserModel).filter(UserModel.id==user_id).first()
#         if not user:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are unnauthorized")
#         return user
#     except:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are unnauthorized")



from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from src.utils.settings import settings
from src.user.modules import UserModel
from src.utils.db import get_db
from jwt.exceptions import InvalidTokenError
import jwt

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