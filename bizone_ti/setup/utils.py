import typing


def get_valid_ti_url(
        ti_url: typing.Union[str, None]) -> typing.Union[str, None]:

    if ti_url is None or ti_url == "":
        return None

    if not ti_url.endswith('/'):
        ti_url += '/'

    if 'api' not in ti_url:
        ti_url += 'api/'

    return ti_url
