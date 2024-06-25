import http
import logging

import fastapi
import uvicorn

from user_service.entrypoints.rest import routers

app = fastapi.FastAPI()
app.include_router(routers.register.router)
app.include_router(routers.login.router)


def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)
