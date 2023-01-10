import re
from os import environ

# Bot information

API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
STRING = environ['STRING_SESSION']

# Admins, Channels & Users

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNEL = environ['AUTH_CHANNEL']
LOG_CHANNEL = environ["LOG_CHANNEL"]

# MongoDB information

DB_URL = environ['DATABASE_URL', 'mongodb+srv://dkbotzon:dkbotzon@cluster0.q9dkemw.mongodb.net/?retryWrites=true&w=majority']
DB_NAME = environ['DATABASE_NAME', 'MrTamilKiD']
