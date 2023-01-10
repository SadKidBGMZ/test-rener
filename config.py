import os

# Bot information

API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH','ea9db4503ed7088b788e06dfd818e00e') 
BOT_TOKEN = os.environ.get('BOT_TOKEN','5623538837:AAFp2qbObz2KgpMSX5By5ai5Xu2FQOnz0xk') 
STRING = os.environ.get("STRING_SESSION","")

# Admins, Channels & Users

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL","-1001551766281"))
ADMIN = int(os.environ.get("ADMIN", 923943045))
CHANNEL = os.environ.get('AUTH_CHANNEL',"")

# MongoDB information

DB_URL = os.environ.get('DATABASE_URL', 'mongodb+srv://dkbotzon:dkbotzon@cluster0.q9dkemw.mongodb.net/?retryWrites=true&w=majority') 
DB_NAME = os.environ.get('DATABASE_NAME', 'MrTamilKiD') 
