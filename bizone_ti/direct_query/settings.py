import typing
from urllib.parse import urlparse

from bizone_ti import setup
from bizone_ti import exceptions


class DirectQuerySettingsSelector:
    TI_URL: typing.Union[str, None] = None
    API_KEY: typing.Union[str, None] = None
    TI_DOMAIN: typing.Union[str, None] = None

    @classmethod
    def select(cls) -> None:
        if (setup.DirectQueryConfig.TI_URL is not None and
           setup.DirectQueryConfig.API_KEY is not None):
            cls.TI_URL = setup.DirectQueryConfig.TI_URL
            cls.API_KEY = setup.DirectQueryConfig.API_KEY

        elif (setup.TILibConfig.TI_URL is not None and
              setup.TILibConfig.API_KEY is not None):
            cls.TI_URL = setup.TILibConfig.TI_URL
            cls.API_KEY = setup.TILibConfig.API_KEY
        else:
            raise exceptions.InvalidAPISettings(
                "Can't find any correct API settings."
                "Please, setup DirectQueryConfig "
                "or TILibConfig first.")

        cls.TI_DOMAIN = urlparse(cls.TI_URL).netloc
