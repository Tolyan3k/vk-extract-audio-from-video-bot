# pylint: disable=invalid-name
"""TODO."""

import functools
import os
import random

import pyotp
import vkaudiotoken
import ZODB
import ZODB.FileStorage
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vkaudiotoken import TokenException

from bot_types.vk_android_audio import VkAndroidApi
from bot_types.zodb_variable import ZodbVariable

# from vk_audio import *
# import pymongo
from config import *

# from bot_types.MongoVariable import MongoVariable


def auth_handler():
    """TODO.

    Returns
    -------
        _type_: _description_

    """
    key = pyotp.TOTP(VK_USER_2FA).now()
    remember_device = True

    return key, remember_device


def captcha_handler(
    captcha,
    vk_bot_session: VkApi,
    vk_bot_group_id: int,
    vk_user_id: int,
):
    """TODO.

    Args:
    ----
        captcha (_type_): _description_
        vk_bot_session (VkApi): _description_
        vk_bot_group_id (int): _description_
        vk_user_id (int): _description_

    Returns:
    -------
        _type_: _description_

    """
    vk_bot_session.get_api().messages.send(
        message="Требуется капча:\n" + f"{captcha.get_url()}",
        user_id=vk_user_id,
        random_id=random.randint(0,
                                 1 << 31),
    )

    key = ""
    for event in VkBotLongPoll(vk_bot_session, vk_bot_group_id).listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_user == vk_user_id:
            key = event.text
            break

    return captcha.try_again(key)


for bot_work_dir in [*BOT_WORK_DIRS.values(), ZODB_DB_DIR]:
    os.makedirs(bot_work_dir, exist_ok=True)

vk_user_session = VkApi(token=VK_USER_TOKEN)
vk_main_group_api_session = VkApi(token=VK_MAIN_GROUP_TOKEN)
vk_archive_group_api_session = VkApi(token=VK_ARCHIVE_GROUP_TOKEN)

captcha_handler = functools.partial(
    captcha_handler,
    vk_bot_session=vk_archive_group_api_session,
    vk_bot_group_id=VK_ARCHIVE_GROUP_ID,
    vk_user_id=VK_USER_ID,
)

try:
    vk_audio_token = vkaudiotoken.get_vk_official_token(
        VK_USER_LOGIN,
        VK_USER_PASSWORD,
        pyotp.TOTP(VK_USER_2FA).now(),
    )["token"]
except (TokenException
        ):    # Если получил код в момент, когда его время действия закончилось
    vk_audio_token = vkaudiotoken.get_vk_official_token(
        VK_USER_LOGIN,
        VK_USER_PASSWORD,
        pyotp.TOTP(VK_USER_2FA).now(),
    )["token"]

vk_audio_api = VkAndroidApi(token=vk_audio_token, secret=VK_AUDIO_CLIENT_SECRET)
vk_audio_api.method("execute.getUserInfo", func_v=9)
vk_audio_api.method("auth.refreshToken", lang="ru")

vk_bot_longpoll = VkBotLongPoll(vk_main_group_api_session, VK_MAIN_GROUP_ID)

if DEBUG:
    DEBUG_VALUE = 1164    # 1047 # 998

    zodb_storage = ZODB.FileStorage.FileStorage(".db/.debug_db")
    zodb_db = ZODB.DB(zodb_storage)

    last_answered_msg_id = ZodbVariable(
        zodb_db=zodb_db,
        var_name="last_answered_message_id",
    )

    error_message_ids = ZodbVariable(
        zodb_db=zodb_db,
        var_name="error_message_ids",
    )

    converted_videos_content_id_to_audio_content_id = ZodbVariable(
        zodb_db=zodb_db,
        var_name="converted_videos_content_id_to_audio_content_id",
    )

    last_answered_msg_id.set_value(DEBUG_VALUE)
    error_message_ids.set_value([])
    if not converted_videos_content_id_to_audio_content_id.exist():
        converted_videos_content_id_to_audio_content_id.set_value({})
else:
    zodb_storage = ZODB.FileStorage.FileStorage(ZODB_DB_PATH)
    zodb_db = ZODB.DB(zodb_storage)

    last_answered_msg_id = ZodbVariable(
        zodb_db=zodb_db,
        var_name="last_answered_message_id",
    )

    error_message_ids = ZodbVariable(
        zodb_db=zodb_db,
        var_name="error_message_ids",
    )

    converted_videos_content_id_to_audio_content_id = ZodbVariable(
        zodb_db=zodb_db,
        var_name="converted_videos_content_id_to_audio_content_id",
    )

    if not last_answered_msg_id.exist():
        last_answered_msg_id.set_value(0)
    if not error_message_ids.exist():
        error_message_ids.set_value([])
    if not converted_videos_content_id_to_audio_content_id.exist():
        converted_videos_content_id_to_audio_content_id.set_value({})

    # db = converted_videos_content_id_to_audio_content_id.get_value()
    # # db.pop('138136673_456239965')
    # converted_videos_content_id_to_audio_content_id.set_value(dict())
