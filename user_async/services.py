from __future__ import annotations

import os

from celery import Celery
from sqlalchemy.exc import IntegrityError

from common.database import SessionLocal
from common.models import User

from common.security import hashing_password


celery_app = Celery("worker", broker=os.getenv('CELERY_BROKER_URL'), backend=os.getenv('CELERY_RESULT_BACKEND'))


@celery_app.task(name='hello_world_task')
def hello_world_task():
    return 'Hello world from Celery!'


@celery_app.task(name='create_user')
def create_user(nickname: str, password: str, info: str):
    db = SessionLocal()

    try:
        user = User(nickname=nickname, hash_password=hashing_password(password), info=info)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user.to_json()
    finally:
        db.close()
