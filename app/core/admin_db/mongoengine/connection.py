from mongoengine import connect, disconnect
from config import settings


def connect_db():
    """
    Connect to database using mongoengine
    """
    connect(
        db=settings.MONGO_NAME,
        host=settings.MONGO_HOST,
        port=int(settings.MONGO_PORT),
        username=settings.MONGO_USERNAME,
        password=settings.MONGO_PASSWORD,
        alias=settings.MONGO_NAME
    )


def disconnect_db():
    """
    Disconnect to database using mongoengine
    """
    disconnect(
        alias=settings.MONGO_NAME
    )
