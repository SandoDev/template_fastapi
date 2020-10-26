from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse
from config.settings import API_VERSION

router = APIRouter()


@router.get("/", tags=["Meta"])
def root():
    return {"MicroService": "FastAPI template"}


@router.get("/version", tags=["Meta"])
def version():
    response = {
        "Version": API_VERSION,
        "Message": "FastAPI template"
    }
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )


@router.get("/health", tags=["Meta"])
def health_check():
    response = {"Status": "Ok"}
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )
