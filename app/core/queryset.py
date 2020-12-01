"""
Querys with pattern repository
"""
from config.settings import database


class QuerysDatabase:
    """
    Querys of DataBase using Motor library
    """

    def __init__(self, collection: str):
        self.collection = database[collection]

    async def save(self, data_to_save):
        doc = await self.collection.insert_one(data_to_save)
        doc_return = await self.collection.find_one({"_id": doc.inserted_id})
        return doc_return

    def get_all(self):
        pass

    def find_by_query(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
