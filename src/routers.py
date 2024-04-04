from fastapi import APIRouter, Depends
from typing import Annotated
from .services import OpenAITools
from .dto import ImagesListDto

validate_router = APIRouter()


@validate_router.post("/validate")
async def validate_images(
    service: Annotated[OpenAITools, Depends()], data: ImagesListDto
):
    return service.send_image_urls_for_validation(data.images_list)
