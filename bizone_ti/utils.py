import logging
import typing

import ujson

logger = logging.getLogger(f"{__name__}")


def try_convert_to_json(
   body: typing.Union[str, dict, None]
   ) -> typing.Union[dict, str]:
    try:
        return ujson.loads(body)
    except ValueError as e:
        logger.exception(e)

    return body
