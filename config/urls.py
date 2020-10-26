from fastapi import APIRouter
from app.api.meta import views as meta
from app.api.v1 import views

urls = APIRouter()

urls.include_router(
    views.router,
    prefix="/api/v1"
)

urls.include_router(
    meta.router,
    prefix=""
)
