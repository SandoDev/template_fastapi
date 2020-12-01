from uuid import uuid4
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class DocumentBase(BaseModel):
    uuid: str = Field(default=str(uuid4()))
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime]


class StudentSchema(DocumentBase):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    class Config:
        name_collection = 'student'
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources engineering",
                "year": 2,
                "gpa": "3.0",
            }
        }
