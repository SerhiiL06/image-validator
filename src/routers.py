from typing import Annotated

from fastapi import APIRouter, Depends

from .dto import ImagesListDto
from .services import OpenAITools

validate_router = APIRouter()


@validate_router.post("/validate")
async def validate_images(
    service: Annotated[OpenAITools, Depends()],
    data: ImagesListDto,
    detail: str = "auto",
):
    return service.send_image_urls_for_validation(data.images_list, detail)
