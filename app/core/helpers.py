def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }


def format_response(response: dict):
    """
    General format for all api responses

    Params
    ------
        response: dict
            - success: bool
                True if the result is as expected
            - message: str
                Service response message
            - data: dict
                Service response data
    """
    return {
        "success": response.get('success'),
        "message": response.get('message'),
        "data": response.get('data_response'),
    }
