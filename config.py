import re
from os import environ

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
