from fastapi import APIRouter
from user_async.services import create_user

router = APIRouter(prefix='/user_async')


@router.post('/add')
def add_user(nickname: str = 'nickname', password: str = 'password', info: str = 'info'):
    task = create_user.apply_async((nickname, password, info))

    return {'task': task.id}


@router.get('/get')
def get_user(nickname: str, password: str):
    pass
