from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="./hello_world/templates")


@router.get('/', response_class=HTMLResponse)
async def hello_world(request: Request):
    return templates.TemplateResponse("hello_world.html", {"request": request})


@router.get('/json')
async def hello_world_json():
    return {"msg": "hello world"}
