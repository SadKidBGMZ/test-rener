import os

class Config:
    ACTIVE_DOWNLOADS = {}
    API_ID = int(os.environ.get("API_ID", '6795023'))
    API_HASH = os.environ.get("API_HASH", '48eb04ae416967495ba9930f87d4f4da')
    PAID_BOT = os.environ.get("PAID_BOT", "YES")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AQDHcnQAjG81efKGAqsDjG6mJrncMF9Tqb7HmWM-9tFDt8Ot4UXEQPaLyarOVd_voUfS05xzZ8ZdVQGr6CORALmLyWSBm7SoV0TxIFxYns4hM-EjithAal1BhyR2HFLwxZiwVpxkYcuLVdI3a87KFJkdORgBNAPwgpz2Q9lNHZTEJmr1a1QMj7t2vakuB96IBwbBCbwCgsNrqBCBxEhbabi8n6PcxxhW39LzMQhj9Ac_NRX8Ak2un9L2c6drMn4qMx0DFL-RDsSh4UWA_UzNol3-R5STVXw0iBaxNCyTUbsNEiX_lYXPWPk3QZ2z2Rs1w3mKpIdGzzipnmKffP-Gg9iJqlZjPwAAAAFB5XkyAA")
    AUTH_USERS =  [int(i) for i in os.environ.get("AUTH_USERS", "5400525106 1504797855").split(" ")]
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5028427286:AAGggDShZZwX7lnfkeaH9i0FalwBBkh2cGU")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://dkbotzon:dkbotzon@cluster0.q9dkemw.mongodb.net/?retryWrites=true&w=majority")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    DB_CHANNEL_ID = -1001769216579
    RESTART_TIME = []
    TIME_GAP1 = {}
    TIME_GAP2 = {}
    timegap_message = {}
