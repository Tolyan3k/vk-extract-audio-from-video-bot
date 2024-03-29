"""TODO."""

from __init__ import (
    vk_audio_api,
    vk_user_session,
)
from bot_types.audio_info import AudioInfo
from vk_api.upload import VkUpload


class VkAudioService:
    """TODO.

    Args:
    ----
        object (_type_): _description_

    Returns:
    -------
        _type_: _description_

    """

    @staticmethod
    def upload_audio(audio_path: str, audio_info: AudioInfo) -> str:
        """TODO.

        Args:
        ----
            audio_path (str): _description_
            audio_info (AudioInfo): _description_

        Returns:
        -------
            str: _description_

        """
        audio_upl_info = VkUpload(vk_user_session).audio(
            audio=audio_path,
            artist=audio_info.artist,
            title=audio_info.title,
        )

        return audio_upl_info["ads"]["content_id"]

    @staticmethod
    def delete_audio(content_id: str) -> None:
        """TODO.

        Args:
        ----
            content_id (str): _description_

        """
        vk_audio_api.method(
            "audio.delete",
            owner_id=content_id.split("_")[0],
            audio_id=content_id.split("_")[1],
        )

    @staticmethod
    def add_audio(content_id: str, to: str = "") -> str | None:
        """TODO.

        Args:
        ----
            content_id (str): _description_
            to (str, optional): _description_. Defaults to "".

        Returns:
        -------
            Optional[str]: _description_

        """
        new_content_id = None

        if to != "":
            result = vk_audio_api.method(
                "audio.add",
                owner_id=content_id.split("_")[0],
                audio_id=content_id.split("_")[1],
                group_id=to,
            )
        else:
            result = vk_audio_api.method(
                "audio.add",
                owner_id=content_id.split("_")[0],
                audio_id=content_id.split("_")[1],
            )

        if len(result) == 1:
            new_content_id = result["response"]

        return new_content_id

    @staticmethod
    def edit_audio(
        audio_content_id: str,
        new_text: str,
        search_visibility: bool,
    ) -> dict:
        # ruff: noqa: FBT001
        """TODO.

        Args:
        ----
            audio_content_id (str): _description_
            new_text (str): _description_
            search_visibility (bool): _description_

        Returns:
        -------
            _type_: _description_

        """
        return vk_audio_api.method(
            "audio.edit",
            owner_id=audio_content_id.split("_")[0],
            audio_id=audio_content_id.split("_")[1],
            no_search=0 if search_visibility else 1,
            text=new_text,
        )["response"]
