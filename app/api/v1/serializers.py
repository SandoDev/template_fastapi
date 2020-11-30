from typing import Optional, List
from pydantic import BaseModel, validator, Field


class ModelOne(BaseModel):
    name: str = Field(
        max_length=50,
        min_length=10,
        description='Name of product'
    )
    description: Optional[str] = None
    price: float
    tax: Optional[float]

    @validator('tax')
    def max_and_min_length(cls, v):
        if v < 0 or v > 1000:
            raise ValueError('Max value 1000 and min value 0')
        return v


class Comment(BaseModel):
    content: int = Field(
        title='contenido del comentario',
        description='este campo almacena un comentario',
    )
    publish: bool = False


class ModelTwo(BaseModel):
    tittle: str = ''
    values: List[Comment]
