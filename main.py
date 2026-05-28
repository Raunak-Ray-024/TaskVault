# from fastapi import FastAPI
# from fastapi.security import HTTPBearer
# from src.utils.db import Base, engine
# from src.task.router import task_routes
# from src.user.router import user_router

# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# security = HTTPBearer()

# app.include_router(task_routes)
# app.include_router(user_router)


from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware # 1. Imported the CORS middleware
from src.utils.db import Base, engine
from src.task.router import task_routes
from src.user.router import user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 2. Configured CORS permissions right after initializing the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows your local HTML files to connect easily
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Allows the critical Authorization header required by HTTPBearer
)

security = HTTPBearer()

app.include_router(task_routes)
app.include_router(user_router)