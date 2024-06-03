from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from user.services import create_user

router = APIRouter(prefix='/user')
templates = Jinja2Templates(directory="./user/templates")


@router.get('/add', response_class=HTMLResponse)
async def add_user_get(request: Request):
    return templates.TemplateResponse("add_user.html", {"request": request})


@router.post('/add', response_class=HTMLResponse)
async def add_user_post(request: Request):
    form_data = await request.form()
    nickname = form_data.get('nickname', 'nickname')
    password = form_data.get('password', 'password')
    info = form_data.get('info', 'info')
    user_db = await create_user(nickname, password, info)
    return templates.TemplateResponse(
        "success.html",
        {"nickname": user_db.nickname, "info": user_db.info, "request": request}
    )

