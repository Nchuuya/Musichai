## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCjPGUQAotmHx2U6fA4EtOIitKQnbViiCAaIzlGX_u19OQRspGKp_JBP_kSVgihPThlOlFEiKllt4azR0HHdYav7GKMNAHIxI2U4MKAJoGWzYqPoUB5Nv4QL4rw1bhcLYBCNvbFmg4FgvpFgtEei0GIa9S8T5C3HJ3AJpMNtx9TL3Sth_zdI1snwqxUt3ad_ibQLT60gwBBRhmxadz8UKu8FBUu5SIg2fcMHjtW8MBltpQlM9hvpt8IPH4xfLv8vsnm7Iuk3LvaOMN92ZZ6XEdHLmYMooiemVAbhgeSN0Wk9vpUP5ydf12QXh-KFR1aG08fAVFN1uNWYUhRwvikY1SMAAAAAHsrA8MA")
BOT_TOKEN = getenv("BOT_TOKEN", "5276474965:AAFGJNgQEWJH1qQ8RlHBNAM9e3aJH7ke18c")
BOT_NAME = getenv("BOT_NAME", "Boa Hancock")
API_ID = int(getenv("API_ID", "8714251"))
API_HASH = getenv("API_HASH", "50c97a11b622575c5b9441b1062f601a")
OWNER_NAME = getenv("OWNER_NAME", "Zhongli ♡ •𝙰𝙷𝙹𝙸𝙽•")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Zerohisooka")
ALIVE_NAME = getenv("ALIVE_NAME", "Boa Hancock ♡")
BOT_USERNAME = getenv("BOT_USERNAME", "BoaHancock_Robot")
OWNER_ID = getenv("OWNER_ID", "5132611794")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Assistant ♡")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "BoaHancock_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "boa_updates")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5132611794").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/de2cba2944d8cbe948d11.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/de2cba2944d8cbe948d11.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Nchuuya/Musichai")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/de2cba2944d8cbe948d11.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/de2cba2944d8cbe948d11.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/de2cba2944d8cbe948d11.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/de2cba2944d8cbe948d11.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/de2cba2944d8cbe948d11.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/de2cba2944d8cbe948d11.jpg")

