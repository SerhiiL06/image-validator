from typing import Annotated

from fastapi import Depends, FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.dto import ImagesListDto
from src.exceptions import SomethingWentWrong
from src.services import OpenAITools

app = FastAPI()


@app.post("/validate")
async def validate_images(
    service: Annotated[OpenAITools, Depends()], data: ImagesListDto
):

    return service.send_images_urls_to_validate(data.images_list)


@app.exception_handler(SomethingWentWrong)
async def server_error_handler(request: Request, exc: SomethingWentWrong):
    return JSONResponse(
        content={f"something went wrong ({exc}). try again"},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
