from uuid import UUID
from .exceptions import ExceptionService
from app.core.queryset import QuerysModelOneMongoEngine as QuerySet
from app.core.queryset import QuerysModelTwoMotor


class ProcessHandler:

    @staticmethod
    def process_one(serializer: dict):
        """
        Just save model
        """
        doc = QuerySet.save(serializer)
        result = {
            "uuid_model": doc.uuid
        }
        return result

    @staticmethod
    def process_four(uuid: str):
        """
        Get model by key
        """
        try:
            uuid_value = UUID(uuid)
        except Exception as e:
            raise ExceptionService(
                success=False,
                message=str(e),
                data={},
                status_code=400
            )
        query = {'uuid': uuid_value}
        model = QuerySet.get_by_query(query=query)
        if model.count() == 0:
            raise ExceptionService(
                success=False,
                message='The document with uuid = ' +
                str(uuid_value)+' does not exist',
                data={},
                status_code=400
            )
        result = {
            "uuid": str(model[0].uuid),
            "name": model[0].name,
            "description": model[0].description,
            "price": model[0].price,
            "tax": model[0].tax
        }
        return result

    @staticmethod
    def process_five(serializer: dict):
        """
        Just save model
        """
        model = QuerysModelTwoMotor()
        doc = model.save(serializer)
        result = {
            "uuid_model": doc.get('uuid')
        }
        return result
