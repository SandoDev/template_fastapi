from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel, Field
from typing import List, Optional


class DocumentBase(BaseModel):
    uuid: str = Field(default=str(uuid4()))
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime]


class Comment(BaseModel):
    content: str = Field(...)
    publish: bool = False


class ModelOne(DocumentBase):
    text: str
    num: int = Field(...)
    comment: Comment
    values: List[str] = []

    class Config:
        orm_mode = True
        collection_name = 'model_one'
