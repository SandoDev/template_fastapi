import os
from datetime import datetime
from uuid import uuid4, UUID
from pydantic import BaseModel, Field
from typing import List
from mongoengine import (
    Document,
    StringField,
    FloatField,
    DateTimeField,
    UUIDField,
    EmbeddedDocument,
    EmbeddedDocumentField
)


class DocumentBase:
    meta = {'db_alias': os.getenv("MONGO_NAME")}
    created_at = DateTimeField(
        default=datetime.now(),
    )
    updated_at = DateTimeField(
        default=datetime.now(),
        null=True
    )


class ModelEmb(EmbeddedDocument):
    uuid_mo = UUIDField(binary=False, default=uuid4)
    name = StringField(default='asd')


class ModelOne(Document, DocumentBase):
    uuid = UUIDField(
        default=uuid4(),
        binary=False,
        # Que sea primary key resulta en que _id: sea este uuid
        primary_key=True
    )
    name = StringField(
        max_length=50,
        min_length=10,
        required=True
    )
    description = StringField(
        required=False,
        default=""
    )
    price = FloatField(
        required=True
    )
    tax = FloatField(
        required=False,
        min_value=0,
        max_value=1000
    )

    meta = {'collection': 'model_one'}


class Comment(BaseModel):
    content: str = Field()
    publish: bool = Field(default=False)


class ModelTwo(BaseModel):
    # TODO guardar uuid como str
    uuid: UUID = Field(default_factory=uuid4)
    tittle: str = Field(required=False)
    values: List[Comment] = Field()

    class Config:
        orm_mode = True
        collection_name = 'model_two'
