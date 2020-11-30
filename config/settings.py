import os
API_VERSION = '1.0'
TIMEZONE = os.getenv("TIMEZONE", None)

"""Database config"""
MONGO_NAME = os.getenv("MONGO_NAME", None)
MONGO_HOST = os.getenv("MONGO_HOST", None)
MONGO_PORT = os.getenv("MONGO_PORT", None)
if '://' in MONGO_HOST:
    HOST_SUB = MONGO_HOST.split('://')[0]
    MONGO_HOST = MONGO_HOST.split('://')[1]
    MONGO_PORT = ''
else:
    HOST_SUB = 'mongodb'

MONGO_USERNAME = os.getenv("MONGO_USERNAME", None)
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", None)
if (MONGO_USERNAME is None or MONGO_USERNAME == '') and \
        (MONGO_PASSWORD is None or MONGO_PASSWORD == ''):
    AUTH = ""
else:
    AUTH = "{user}:{password}@".format(
        user=MONGO_USERNAME, password=MONGO_PASSWORD)
