from pydantic import BaseModel, Field, validator
from typing import List, Optional


class Comment(BaseModel):
    content: str = Field(...)
    publish: bool = False


class ModelOne(BaseModel):
    text: str
    num: int = Field(...)
    comment: Comment
    values: List[str] = []


class ModelTwo(BaseModel):
    name: str = Field(
        max_length=50,
        min_length=10,
        description='Name of product',
    )
    description: Optional[str] = None
    price: float
    tax: Optional[float]

    @validator('tax')
    def max_and_min_length(cls, v):
        if v < 0 or v > 1000:
            raise ValueError('Max value 1000 and min value 0')
        return v
