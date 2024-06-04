from __future__ import annotations


from common.database import SessionLocal
from common.models import User

from common.security import hashing_password


async def create_user(nickname: str, password: str, info: str) -> User | None:
    db = SessionLocal()

    try:
        user = User(nickname=nickname, hash_password=hashing_password(password), info=info)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    finally:
        db.close()
