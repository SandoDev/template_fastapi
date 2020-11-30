"""
Querys with pattern repository
"""
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

    TODO las clases deberían ser iguales en su estructura,
    se podría usar herencia on interfases
    """

    def __init__(self):
        self.cli_conn = None

    def cli_bd(self):
        # TODO como se usa el patron sigleton?
        if self.cli_conn is None:
            self.cli_conn = connect_db()
            return self.cli_conn
        return self.cli_conn

    def save(self, data_to_save: dict):
        model = ModelTwo(**data_to_save)
        collection = model.__config__.collection_name
        model_dict = model.dict()
        self.cli_bd()[collection].insert_one(model_dict)
        return model_dict

    def __init__(self):
        self.cli_conn = None
        self.collection = StatusGuarantor.__config__.collection_name

    def cli_bd(self):
        if self.cli_conn is None:
            self.cli_conn = 0  # TODO cambiar
            return self.cli_conn
        return self.cli_conn

    def save(self, data_to_save: dict):
        """
        Save model on db
        """
        model = StatusGuarantor(**data_to_save)
        model_dict = model.dict()
        self.cli_bd()[self.collection].insert_one(model_dict)
        return model_dict

    async def find_by_query(self, query: dict):
        """
        Get one document by query of db
        """
        doc = await self.cli_bd()[self.collection].find_one(query)
        return doc
