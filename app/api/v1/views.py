from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from app.api.v1.serializers import (
    SerializerStudent,
    UpdateStudentModel,
)
from app.core.handlers import ProcessHandler
from app.core.helpers import format_response

router = APIRouter()


@router.post(
    "/add_student",
    summary="save model",
    description="Save model with motor and pydantic",
    response_class=JSONResponse,
    tags=["Endpoints"],
)
async def add_student(student: SerializerStudent = Body(...)):
    student = jsonable_encoder(student)
    new_student = await ProcessHandler.add_student(student)
    return format_response(
        {
            'success': True,
            'message': 'Student added successfully.',
            'data_response': new_student
        }
    )
