import fastapi
from template_service import views

router = fastapi.APIRouter()


@router.get("/", status_code=fastapi.status.HTTP_200_OK)
async def index() -> fastapi.responses.HTMLResponse:
    markdown_content = views.get_index()

    return fastapi.responses.HTMLResponse(content=markdown_content)
