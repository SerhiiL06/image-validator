from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from src.routers import validate_router

from src.exceptions import SomethingWentWrong, BadRequest

app = FastAPI()


app.include_router(validate_router)


@app.exception_handler(SomethingWentWrong)
async def server_error_handler(request: Request, exc: SomethingWentWrong):
    error_message = f"something went wrong ({exc}). try again"
    return JSONResponse(
        content=error_message,
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


@app.exception_handler(BadRequest)
async def server_error_handler(request: Request, exc: BadRequest):
    error_message = "your request was wrong, please try again"
    return JSONResponse(
        content=error_message,
        status_code=exc.code,
    )
