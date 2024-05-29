from fastapi import APIRouter
from user.services import create_user

router = APIRouter(prefix='user')


@router.post('/add')
def add_user(nickname: str = 'nickname', password: str = 'password', info: str = 'info'):
    user_db = create_user(nickname, password, info)

    return {'New user': user_db}
