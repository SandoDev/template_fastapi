import os
from mongoengine import connect, disconnect


def connect_db():
    """
    Connect to database using mongoengine
    """
    connect(
        db=os.getenv('MONGO_NAME'),
        host=os.getenv('MONGO_HOST'),
        port=int(os.getenv('MONGO_PORT')),
        username=os.getenv('MONGO_USERNAME'),
        password=os.getenv("MONGO_PASSWORD"),
        alias=os.getenv('MONGO_NAME')
    )


def disconnect_db():
    """
    Disconnect to database using mongoengine
    """
    disconnect(
        alias=os.getenv('MONGO_NAME')
    )
