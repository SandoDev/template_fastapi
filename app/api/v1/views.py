from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from app.api.v1.serializers import (
    ModelOne,
    ModelTwo
)
from app.core.handlers import ProcessHandler
from app.core.responses import format_response

router = APIRouter()


@router.post(
    "/endpoint_one",
    summary="Summary",
    description="Description of endpoint",
    response_class=JSONResponse,
    tags=["Endpoints"],
)
def endpoint_one(model: ModelOne):
    model_dict = jsonable_encoder(model)
    return format_response(
        {
            'success': True,
            'message': 'full response',
            'data_response': model_dict
        }
    )


@router.post(
    "/endpoint_two",
    summary="Summary",
    description="Description of endpoint",
    response_class=JSONResponse,
    tags=["Endpoints"],
    response_model=ModelOne,
)
def endpoint_two(model: ModelOne):
    model_dict = jsonable_encoder(model)
    return model_dict


@router.post(
    "/endpoint_three",
    summary="save model",
    description="save model with mongoengine",
    response_class=JSONResponse,
    tags=["Endpoints"],
)
def endpoint_three(model: ModelOne):
    model_dict = jsonable_encoder(model)
    result = ProcessHandler.process_one(
        model_dict
    )
    return format_response(
        {
            'success': True,
            'message': 'Registro guardado',
            'data_response': result
        }
    )


@router.get(
    "/endpoint_four/{uuid}",
    summary="get model",
    description="Description of endpoint",
    response_class=JSONResponse,
    tags=["Endpoints"],
)
def endpoint_four(uuid: str):
    result = ProcessHandler.process_four(uuid)
    return format_response(
        {
            'success': True,
            'message': 'full response',
            'data_response': jsonable_encoder(result)
        }
    )


@router.post(
    "/endpoint_five",
    summary="save model",
    description="Save model with motor and pydantic",
    response_class=JSONResponse,
    tags=["Endpoints"],
)
async def endpoint_five(model: ModelTwo):
    model_dict = jsonable_encoder(model)
    result = ProcessHandler.process_five(
        model_dict
    )
    return format_response(
        {
            'success': True,
            'message': 'Registro guardado',
            'data_response': result
        }
    )
