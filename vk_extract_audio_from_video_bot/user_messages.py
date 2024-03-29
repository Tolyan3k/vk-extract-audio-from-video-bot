"""TODO."""

import config


def start_processing_message() -> str:
    """TODO.

    Returns
    -------
        str: _description_

    """
    return "Начинаю обработку сообщения..."


def undefined_convert_error() -> str:
    """TODO.

    Returns
    -------
        str: _description_

    """
    return "Произошла непредвиденная ошибка во время конвертации сообщения."


def videos_not_found() -> str:
    """TODO.

    Returns
    -------
        str: _description_

    """
    return "Не удалось найти видео в сообщении"


def video_not_support() -> str:
    """TODO.

    Returns
    -------
        str: _description_

    """
    return (
        "К сожалению, данное видео не поддерживается ботом."
        " Или возможно, что оно не содержит аудио."
    )


def failed_to_convert_part_many() -> str:
    """TODO.

    Returns
    -------
        str: _description_

    """
    return (
        "К сожалению, часть видео не удалось сконвертировать.\n"
        "Возможно, некоторые видео слишком длинные (>"
        f" {config.VIDEO_MAX_DURATION / 60!s}"
        " минут), либо их платформа не поддерживается."
    )


def failed_to_convert_all_many() -> str:
    """TODO.

    Returns
    -------
        str: _description_

    """
    return (
        "К сожалению, боту не удалось сконвертировать в аудио ни одно видео.\n"
        "Это может быть связяно с тем, что платформы этих видео сейчас"
        " не поддерживаются ботом, либо видео длиннее"
        f" {config.VIDEO_MAX_DURATION / 60!s} минут."
    )
