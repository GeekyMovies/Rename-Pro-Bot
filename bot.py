from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "AAF9MzN2Mk8QQhkalABpz_45MjQjBnQUOqg")

APP_ID = int(os.environ.get("APP_ID", "23311160"))

API_HASH = os.environ.get("API_HASH", "2a1366013eca4256bce853346dbcda49")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
