# from fastapi import FastAPI
# from src.utils.db import Base, engine  #Base-ORM base class (enables automatic table creation) and engine is the database connection object
# # from src.task.modules import TaskModel
# from src.task.router import task_routes #responsible for the endpoints 
# from src.user.router import user_router


# Base.metadata.create_all(bind=engine)  #creates table if not exists

# app=FastAPI()

# app.include_router(task_routes) #registers all routes from task_routes to  main app
# app.include_router(user_router)


from fastapi import FastAPI
from fastapi.security import HTTPBearer
from src.utils.db import Base, engine
from src.task.router import task_routes
from src.user.router import user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

security = HTTPBearer()

app.include_router(task_routes)
app.include_router(user_router)


# from fastapi import FastAPI
# from fastapi.openapi.utils import get_openapi
# from src.utils.db import Base, engine
# from src.task.router import task_routes
# from src.user.router import user_router

# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# app.include_router(task_routes)
# app.include_router(user_router)

# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         title="FastAPI",
#         version="0.1.0",
#         routes=app.routes,
#     )
#     openapi_schema["components"]["securitySchemes"] = {
#         "BearerAuth": {
#             "type": "http",
#             "scheme": "bearer"
#         }
#     }
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema

# app.openapi = custom_openapi