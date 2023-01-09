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
STRING = environ['STRING_SESSION', 'BQDMOvAACtNs-VchfumyK9k5-nCNC07ktlBNprSCibT8v6TlKUld6ZCdmSweiwaB9dYKGUGUDJoVmwk76Di47l9KaeEfBO_6ly7autQqKVoaV0t51FOqxtQQ5sm1zKT4qfvV0zUnw-2nY4yUEzCJJ-2OADSkzQXUDWq_0R1WEDvDOrwUVu6Q92Yliu3yOvUe-yYF9Cd9aiUZO8oOl2Lr5ljVBOQXD1s-acZV_80Ltf20fTkuYym6Bv1zrdvyXuyiBBaQKv_cwHaXcjmAlxvmQaBE-N75q8C_TazXigo0Uflhpqj7MzZoLJZQWw15Tci7RITeErIKtRFC7u6JhnbLDIEZ_uuWYgAAAABZsWSfAA']

# Admins, Channels & Users

ADMIN =  [int(i) for i in os.environ.get("AUTH_USERS", "5400525106 1504797855").split(" ")]
CHANNEL = os.environ.get('AUTH_CHANNEL')
LOG_CHANNEL = os.environ.get("LOG_CHANNEL") 

# MongoDB information

DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://dkbotzon:dkbotzon@cluster0.q9dkemw.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "MrTamilKiD")
