import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5377834462:AAFr_4q9Sw3RtGPoMtgkxy-w4A6TE8oN_0w")

API_ID = int(os.environ.get("API_ID", "13384432"))

API_HASH = os.environ.get("API_HASH", "ea9db4503ed7088b788e06dfd818e00e")

STRING = os.environ.get("STRING", "AQDHcnQAjG81efKGAqsDjG6mJrncMF9Tqb7HmWM-9tFDt8Ot4UXEQPaLyarOVd_voUfS05xzZ8ZdVQGr6CORALmLyWSBm7SoV0TxIFxYns4hM-EjithAal1BhyR2HFLwxZiwVpxkYcuLVdI3a87KFJkdORgBNAPwgpz2Q9lNHZTEJmr1a1QMj7t2vakuB96IBwbBCbwCgsNrqBCBxEhbabi8n6PcxxhW39LzMQhj9Ac_NRX8Ak2un9L2c6drMn4qMx0DFL-RDsSh4UWA_UzNol3-R5STVXw0iBaxNCyTUbsNEiX_lYXPWPk3QZ2z2Rs1w3mKpIdGzzipnmKffP-Gg9iJqlZjPwAAAAFB5XkyAA") 



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
