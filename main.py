from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.exceptions import BadRequest, SomethingWentWrong
from src.routers import validate_router

app = FastAPI()


app.include_router(validate_router)


@app.exception_handler(SomethingWentWrong)
async def server_error_handler(request: Request, exc: SomethingWentWrong):
    error_message = {"code": 500, "message": f"something went wrong ({exc}). try again"}
    return JSONResponse(
        content=error_message,
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


@app.exception_handler(BadRequest)
async def server_error_handler(request: Request, exc: BadRequest):
    error_message = {"code": exc.code, "message": "wrong request, no valid link"}
    return JSONResponse(
        content=error_message,
        status_code=exc.code,
    )
