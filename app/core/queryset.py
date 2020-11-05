"""
Querys with pattern repository
"""
from .admin_db.motor.connection import connect_db
from .models import ModelOne, ModelTwo


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
        self.cli_conn = None

    def cli_bd(self):
        if self.cli_conn is None:
            self.cli_conn = connect_db()
            return self.cli_conn
        return self.cli_conn

    def save(self, data_to_save: dict):
        model = ModelTwo(**data_to_save)
        collection = model.__class__.__name__
        model_dict = model.dict()
        self.cli_bd()[collection].insert_one(model_dict)
        return model_dict
