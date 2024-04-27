import uvicorn
from fastapi import FastAPI

from containers import Services
from controllers import health_controller, ocr_controller

app = FastAPI(title="AI course final project, by Hussein Cheayto.")

services = Services()
services.wire(modules=[health_controller, ocr_controller])
app.services = services

app.include_router(health_controller.router, prefix="/health", tags=["Health"])
app.include_router(ocr_controller.router, prefix="/ocr", tags=["Optical Character Recognition"])

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
