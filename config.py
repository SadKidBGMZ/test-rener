import os

# Bot information

API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH') 
BOT_TOKEN = os.environ.get('BOT_TOKEN','') 
STRING = os.environ.get("STRING_SESSION","")

# Admins, Channels & Users

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL",""))
ADMIN = int(os.environ.get("ADMIN", 923943045))
CHANNEL = os.environ.get('AUTH_CHANNEL',"")

# MongoDB information

DB_URL = os.environ.get('DATABASE_URL', 'mongodb+srv://dkbotzon:dkbotzon@cluster0.q9dkemw.mongodb.net/?retryWrites=true&w=majority') 
DB_NAME = os.environ.get('DATABASE_NAME', 'MrTamilKiD') 
