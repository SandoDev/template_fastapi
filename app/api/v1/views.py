from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


def format_response(response: dict, success: bool = True):
    return {
        "code": response.get('status_code'),
        "message": response.get('message'),
        "data": response.get('data_response'),
    }


@router.get(
    "/endpoint_one",
    response_class=JSONResponse,
    tags=['Endpoints']
)
def endpoint_one(uuid: str = ''):
    return format_response(
        {
            'status_code': 200,
            'message': 'todo full',
            'data_response': uuid
        },
        True
    )
