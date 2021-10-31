import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "BI0xX_NETWORK")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cb45b1b9c1e30a7eac7e1.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ɮɨ0 x✘")
OWNER_NAME = getenv("OWNER_NAME", "SOUL_BI0xX")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "BI0xX_NETWORK")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlayBot2.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/heaven2hellx/BI0xXMUSIC")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2059580545").split()))
