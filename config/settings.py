import os
import motor.motor_asyncio as motor

"""Global vars"""
API_VERSION = '1.0'
TIMEZONE = os.getenv("TIMEZONE", None)

"""Database config"""
MONGO_NAME = os.getenv("MONGO_NAME", None)
MONGO_HOST = os.getenv("MONGO_HOST", None)
MONGO_PORT = os.getenv("MONGO_PORT", None)
MONGO_USERNAME = os.getenv("MONGO_USERNAME", None)
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", None)

# Config for DNS Seed List Connection Format
if '://' in MONGO_HOST:
    HOST_SUB = MONGO_HOST.split('://')[0]
    MONGO_HOST = MONGO_HOST.split('://')[1]
    MONGO_PORT = ''
else:
    HOST_SUB = 'mongodb'
    MONGO_PORT = ':' + MONGO_PORT

# Config user and pass mongo
if (MONGO_USERNAME is None or MONGO_USERNAME == '') and \
        (MONGO_PASSWORD is None or MONGO_PASSWORD == ''):
    AUTH = ""
else:
    AUTH = "{user}:{password}@".format(
        user=MONGO_USERNAME, password=MONGO_PASSWORD)

# Config URI connection to mongo
URL = "{host_sub}://{auth}{host}{port}".format(
    host_sub=HOST_SUB,
    auth=AUTH,
    host=MONGO_HOST,
    port=MONGO_PORT,
)

"""Config db with motor library"""
client = motor.AsyncIOMotorClient(URL)
database = client[MONGO_NAME]
