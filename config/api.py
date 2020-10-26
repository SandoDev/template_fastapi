from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.settings import API_VERSION
from config.urls import urls

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
