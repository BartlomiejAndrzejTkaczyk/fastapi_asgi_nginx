from fastapi import FastAPI
from user_async.router import router as user_async_router
from user.router import router as user_router
from hello_world.router import router as hello_world_router
from loader_io.router import router as loader_io_router

app = FastAPI()
app.include_router(user_async_router)
app.include_router(user_router)
app.include_router(hello_world_router)
app.include_router(loader_io_router)

