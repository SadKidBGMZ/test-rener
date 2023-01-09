import os

    API_ID = int(os.environ.get("API_ID", '6795023'))

    API_HASH = os.environ.get("API_HASH", '48eb04ae416967495ba9930f87d4f4da')

    STRING = os.environ.get("STRING_SESSION", "BQDMOvAACtNs-VchfumyK9k5-nCNC07ktlBNprSCibT8v6TlKUld6ZCdmSweiwaB9dYKGUGUDJoVmwk76Di47l9KaeEfBO_6ly7autQqKVoaV0t51FOqxtQQ5sm1zKT4qfvV0zUnw-2nY4yUEzCJJ-2OADSkzQXUDWq_0R1WEDvDOrwUVu6Q92Yliu3yOvUe-yYF9Cd9aiUZO8oOl2Lr5ljVBOQXD1s-acZV_80Ltf20fTkuYym6Bv1zrdvyXuyiBBaQKv_cwHaXcjmAlxvmQaBE-N75q8C_TazXigo0Uflhpqj7MzZoLJZQWw15Tci7RITeErIKtRFC7u6JhnbLDIEZ_uuWYgAAAABZsWSfAA")

    ADMIN =  [int(i) for i in os.environ.get("AUTH_USERS", "5400525106 1504797855").split(" ")]

    CHANNEL = os.environ.get('AUTH_CHANNEL')

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5028427286:AAGggDShZZwX7lnfkeaH9i0FalwBBkh2cGU")

    DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://dkbotzon:dkbotzon@cluster0.q9dkemw.mongodb.net/?retryWrites=true&w=majority")

    DB_NAME = os.environ.get("DATABASE_NAME", "MrTamilKiD")

    LOG_CHANNEL = os.environ.get("LOG_CHANNEL") 
