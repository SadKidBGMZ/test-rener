import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information

API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
STRING = environ['STRING_SESSION']

# Admins, Channels & Users

ADMIN =  [int(i) for i in os.environ.get("AUTH_USERS", "5400525106 1504797855").split(" ")]
CHANNEL = environ['AUTH_CHANNEL']
LOG_CHANNEL = environ["LOG_CHANNEL"]

# MongoDB information

DB_URL = environ['DATABASE_URL', 'mongodb+srv://dkbotzon:dkbotzon@cluster0.q9dkemw.mongodb.net/?retryWrites=true&w=majority']
DB_NAME = environ['DATABASE_NAME', 'MrTamilKiD']
