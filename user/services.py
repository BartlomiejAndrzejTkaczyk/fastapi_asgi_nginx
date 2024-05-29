from __future__ import annotations

from sqlalchemy.exc import IntegrityError

from common.database import SessionLocal
from user.expections import UserExistsException
from user_async.models import User

from common.security import hashing_password


def find_user_by(nickname: str) -> User | None:
    db = SessionLocal()
    user = db.query(User).filter(User.nickname == nickname).first()

    return user


def create_user(nickname: str, password: str, info: str) -> User | None:
    db = SessionLocal()

    is_exists = find_user_by(nickname=nickname) is not None
    if is_exists:
        raise UserExistsException()

    try:
        user = User(nickname=nickname, hash_password=hashing_password(password), info=info)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise UserExistsException()
    finally:
        db.close()
