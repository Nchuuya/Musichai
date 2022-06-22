## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBAl2qFvgEqUoNMarWKGL91qpXqhfjTAG1LwA4hOBnDs7ghKBqR_Znc_BNgXw9sLjflIX3wGs6qBZylghW5U5WR4cjQGE6uhT4gm8QhIS4c-2oNg6ML96Re2K9YRCQF1_q-AMzUvvuyk_UwaaMkDLFk7QL3iwkX-QjzNGk551CxyRfS9afdy5zxwaY-R0lBbDEF4qhwXmtnpD35pbc-wX0-d3sbmjiq7T7gVZRMEAHPkoGtQ_NOTR9bwRvFR1Ac3_dwgNaZ5Knm3Vs7uMeBFMX-6zAc22XLnbvVqTqcv-rB1zvy1Z-gxioZYUjflDBJpLUqYSLLVSTRAaJ1Q62yOCMvAAAAAUBQ4EMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5533385439:AAFGV_cJWfG03fb1Mj55PqAI0pGfXJfzMag")
BOT_NAME = getenv("BOT_NAME", "@AsukaRobot")
API_ID = int(getenv("API_ID", "10501678"))
API_HASH = getenv("API_HASH", "c28923c93d9f26ad3fa920972f3a989f")
OWNER_NAME = getenv("OWNER_NAME", "Xelcius")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Xelcius")
ALIVE_NAME = getenv("ALIVE_NAME", "Asuka")
BOT_USERNAME = getenv("BOT_USERNAME", "AsukaRobot")
OWNER_ID = getenv("OWNER_ID", "5132611794")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "AsukaAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AsukaSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Anime_Cruise")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5132611794").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RimuruDemonlord/VcBot")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
