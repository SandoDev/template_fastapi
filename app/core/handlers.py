from .queryset import QuerysDatabase as QuerySet
from .helpers import student_helper


class ProcessHandler:

    @staticmethod
    async def add_student(student_data: dict) -> dict:
        q = QuerySet('student')
        doc = await q.save(student_data)
        return student_helper(doc)
