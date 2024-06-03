from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get('/loaderio-b870ca900bf56f434c0db90bf2f6961a/', response_class=HTMLResponse)
def loader_io():
    html_content = 'loaderio-b870ca900bf56f434c0db90bf2f6961a'
    return HTMLResponse(content=html_content, status_code=status.HTTP_200_OK)

