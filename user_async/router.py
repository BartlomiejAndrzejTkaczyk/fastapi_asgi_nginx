from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from user_async.services import create_user

router = APIRouter(prefix='/user_async')
templates = Jinja2Templates(directory="./user_async/templates")


@router.get('/add', response_class=HTMLResponse)
async def add_user_get(request: Request):
    return templates.TemplateResponse("add_user_async.html", {"request": request})


@router.post('/add', response_class=HTMLResponse)
async def add_user_post(request: Request):
    form_data = await request.form()
    nickname = form_data.get('nickname', 'nickname')
    password = form_data.get('password', 'password')
    info = form_data.get('info', 'info')
    task = create_user.apply_async((nickname, password, info))
    return templates.TemplateResponse("success_async.html", {"task_id": task.id, "request": request})
