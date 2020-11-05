"""
Querys with pattern repository
"""
from .models import ModelOne


class QuerysModelOneMongoEngine:
    """
    Querys of ModelOne using mongoengine library
    """

    @classmethod
    def save(cls, data_to_save: dict):
        model = ModelOne(**data_to_save)
        doc = model.save()
        return doc

    @classmethod
    def get_by_query(cls, query: dict):
        docs = ModelOne.objects(**query)
        return docs


class QuerysModelTwoMotor:
    """
    Querys of ModelOne using Motor library
    """

    def __init__(self):
        self.orm = ModelOne()

    def save(self, data):
        doc = self.orm.save(data)
        return doc
