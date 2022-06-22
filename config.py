import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
if str(getenv("SESSION_NAME")).strip() == "AQBAl2qFvgEqUoNMarWKGL91qpXqhfjTAG1LwA4hOBnDs7ghKBqR_Znc_BNgXw9sLjflIX3wGs6qBZylghW5U5WR4cjQGE6uhT4gm8QhIS4c-2oNg6ML96Re2K9YRCQF1_q-AMzUvvuyk_UwaaMkDLFk7QL3iwkX-QjzNGk551CxyRfS9afdy5zxwaY-R0lBbDEF4qhwXmtnpD35pbc-wX0-d3sbmjiq7T7gVZRMEAHPkoGtQ_NOTR9bwRvFR1Ac3_dwgNaZ5Knm3Vs7uMeBFMX-6zAc22XLnbvVqTqcv-rB1zvy1Z-gxioZYUjflDBJpLUqYSLLVSTRAaJ1Q62yOCMvAAAAAUBQ4EMA":
    SESSION_NAME = str(None)
else:
    SESSION_NAME = str(getenv("SESSION_NAME"))

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5533385439:AAFGV_cJWfG03fb1Mj55PqAI0pGfXJfzMag")
BOT_NAME = getenv("BOT_NAME", "@AsukaRobot")

API_ID = int(getenv("API_ID", "10501678"))
API_HASH = getenv("API_HASH", "c28923c93d9f26ad3fa920972f3a989f")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Xelcius")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Xelcius")
ALIVE_NAME = getenv("ALIVE_NAME", "Asuka")
BOT_USERNAME = getenv("BOT_USERNAME", "AsukaRobot")
OWNER_ID = getenv("OWNER_ID", "5330764294")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "AsukaAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AsukaSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Anime_Cruise")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5132611794").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
