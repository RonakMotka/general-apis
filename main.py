from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
# from fastapi_utils.tasks import repeat_every

from routers.admin.v1 import api as admin_v1
# from routers.admin.v1.crons.scheduled_notifications import (
#     check_scheduled_notifications,
#     clear_sent_notifications,
# )

app = FastAPI(
    title="GENERAL",
    description="APIs for Admin",
    version="1.0.0",
    # docs_url=None,
    redoc_url=None,
)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.on_event("startup")
# @repeat_every(seconds=10800, wait_first=True)  # Every 3 hours
# def scheduled_notifications_task() -> None:
#     check_scheduled_notifications()


# @app.on_event("startup")
# @repeat_every(seconds=43200, wait_first=True)  # Every 12 hours
# def clear_scheduled_notifications_task() -> None:
#     clear_sent_notifications()


app.include_router(admin_v1.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error = exc.errors()[0]
    field = str(error["loc"][1])
    message = error["msg"]
    detail = field + " - " + message.capitalize()
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": detail}),
    )
