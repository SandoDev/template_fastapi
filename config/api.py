from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from starlette import status
from starlette.exceptions import HTTPException as StarletteHTTPException
from config.settings import API_VERSION
from config.urls import urls
from app.core.responses import format_response


app = FastAPI(
    title="FastAPI template of microservices",
    description="This is a template for build microservices with FastAPI",
    version=API_VERSION,
    redoc_url="/api/v1/redoc",
    docs_url='/api/v1/docs',
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    urls
)


@app.exception_handler(Exception)
async def exception_handler(request, exc):
    data = {}
    if len(exc.args) == 4:
        code_status = exc.args[3]
        data["success"] = exc.args[0]
        data["message"] = exc.args[1]
        data["data_response"] = exc.args[2]
    else:
        code_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        data["success"] = False
        data["message"] = str(exc.args)
        data["data_response"] = {}

    return JSONResponse(
        status_code=code_status,
        content=jsonable_encoder(
            format_response(data)
        ),
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print()
    print('Si alguna vez aparece esto haganmelo saber, sandodev')
    print()
    data = {
        "codRespuesta": exc.status_code,
        "observaciones": str(exc.detail)
    }

    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(
            format_response(data)
        ),
    )
