from http import HTTPStatus
import typing


class HTTPSessionConfig:
    HTTP_PROXY = None
    HTTPS_PROXY = None
    RETRY_TIMES = 10
    BACKOFF_FACTOR = 2
    STATUS_FORCELIST = [
        HTTPStatus.REQUEST_TIMEOUT.value,
        HTTPStatus.CONFLICT.value,
        HTTPStatus.TOO_EARLY.value,
        HTTPStatus.TOO_MANY_REQUESTS.value,
        HTTPStatus.INTERNAL_SERVER_ERROR.value,
        HTTPStatus.BAD_GATEWAY.value,
        HTTPStatus.SERVICE_UNAVAILABLE.value,
        HTTPStatus.GATEWAY_TIMEOUT.value,
    ]
    HTTP_SUCCESS_CODES = [
        HTTPStatus.OK.value,
        HTTPStatus.ACCEPTED.value,
        HTTPStatus.CREATED.value,
    ]

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(HTTPSessionConfig, cls).__new__(
                cls, *args, **kwargs)
        return cls.instance

    def setup(
        self,
        http_proxy: typing.Union[str, None] = None,
        https_proxy: typing.Union[str, None] = None,
        retry_times: typing.Union[int, None] = None,
        backoff_factor: typing.Union[int, None] = None,
        status_forcelist: typing.Union[list[int], None] = None
    ) -> None:
        self.HTTP_PROXY = http_proxy
        self.HTTPS_PROXY = https_proxy
        self.RETRY_TIMES = retry_times or self.RETRY_TIMES
        self.BACKOFF_FACTOR = backoff_factor or self.BACKOFF_FACTOR
        self.STATUS_FORCELIST = status_forcelist or self.STATUS_FORCELIST
