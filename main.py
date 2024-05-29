def must_be_first():
    import os
    import dotenv

    if os.getenv('CELERY_BROKER_URL') is None:
        dotenv.load_dotenv()


must_be_first()

from fastapi import FastAPI
from user_async.router import router as user_async_router

app = FastAPI()
app.include_router(user_async_router)


@app.get('/')
def hello_world():
    return {'hello_world': 200}
