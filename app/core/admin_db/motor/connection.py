from config import settings
import motor.motor_asyncio as motor


def connect_db():
    """
    Connect to database using motor
    """
    url = "mongodb://{auth}{host}:{port}/{db_name}".format(
        auth=settings.AUTH,
        host=settings.MONGO_HOST,
        port=settings.MONGO_PORT,
        db_name=settings.MONGO_NAME
    )
    client = motor.AsyncIOMotorClient(url)
    return client[settings.MONGO_NAME]


# def disconnect_db():
#     """
#     Disconnect to database using mongoengine
#     """
#     disconnect(
#         alias=os.getenv('MONGO_NAME')
#     )
