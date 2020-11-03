from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from littlenv import littlenv

from config.settings import API_VERSION
from config.urls import urls
from app.core.admin_db.mongoengine.connection import connect_db, disconnect_db
from app.core.responses import format_response


littlenv.load()

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

app.add_event_handler(
    "startup",
    connect_db
)

app.add_event_handler(
    "shutdown",
    disconnect_db
)


@app.exception_handler(Exception)
async def exception_handler(request, exc):
    data = {}
    code_status = exc.args[3]
    data["success"] = exc.args[0]
    data["message"] = exc.args[1]
    data["data"] = exc.args[2]

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
