import typing


class TIConfig:
    TI_URL = None
    API_KEY = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(TIConfig, cls).__new__(
                cls, *args, **kwargs)
        return cls.instance

    def setup(self,
              ti_url: typing.Union[str, None] = None,
              api_key: typing.Union[str, None] = None) -> None:
        self.TI_URL = ti_url
        self.API_KEY = api_key
