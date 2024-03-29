"""TODO."""

import os

# VK USER CONFIG
VK_USER_TOKEN = os.environ["VK_USER_TOKEN"]
VK_USER_LOGIN = os.environ["VK_USER_LOGIN"]
VK_USER_PASSWORD = os.environ["VK_USER_PASSWORD"]
VK_USER_2FA = os.environ["VK_USER_2FA"]
VK_USER_ID = os.environ["VK_USER_ID"]

# VK ARCHIVE GROUP CONFIG
VK_ARCHIVE_GROUP_TOKEN = os.environ["VK_ARCHIVE_GROUP_TOKEN"]
VK_ARCHIVE_GROUP_ID = os.environ["VK_ARCHIVE_GROUP_ID"]

# VK MAIN GROUP CONFIG
VK_MAIN_GROUP_URL = os.environ["VK_MAIN_GROUP_URL"]
VK_MAIN_GROUP_TOKEN = os.environ["VK_MAIN_GROUP_TOKEN"]
VK_MAIN_GROUP_ID = os.environ["VK_MAIN_GROUP_ID"]

# VK AUDIO CLIENT CONFIG
VK_AUDIO_CLIENT_SECRET = os.environ["VK_AUDIO_CLIENT_SECRET"]

# BOT DIRECTORIES CONFIG
BOT_DIR = os.environ["PYTHONPATH"]
BOT_WORK_DIRS = {
    "videos": BOT_DIR + "/.temp/videos",
    "audios": BOT_DIR + "/.temp/audios",
}

# DATABASE CONFIG
ZODB_DB_DIR = f"{BOT_DIR}/{os.environ['ZODB_DB_DIR']}"
ZODB_DB_NAME = os.environ["ZODB_DB_NAME"]
ZODB_DB_PATH = f"{ZODB_DB_DIR}/{ZODB_DB_NAME}"

# VIDEO LENGHT CONFIG (in seconds)
VIDEO_MIN_DURATION = 0
VIDEO_MAX_DURATION = int(os.environ["VIDEO_MAX_DURATION"])

# 10 HOURS (in seconds)
VIDEO_MAX_GENERAL_DURATION = 10 * 3600

# AUDIO LENGTH CONFIG (in seconds)
AUDIO_MIN_DURATION = 5

# VK OVERALL CONFIG
VK_MAX_ATTACHMENTS = 10
VK_MAX_AUDIOFILE_SIZE_MB = 200    # in MB
