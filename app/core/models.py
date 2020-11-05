import os
from datetime import datetime
from uuid import uuid4
from mongoengine import (
    Document,
    StringField,
    FloatField,
    DateTimeField,
    UUIDField,
    ListField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    BooleanField
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


class Comment(EmbeddedDocument):
    content = StringField(
        required=True
    )
    publish = BooleanField(
        default=False
    )


class ModelTwo(Document, DocumentBase):
    uuid = UUIDField(
        default=uuid4(),
        binary=False,
    )
    tittle = StringField(
        required=False,
        default=''
    )
    values = ListField(
        EmbeddedDocumentField(Comment),
        required=True
    )
