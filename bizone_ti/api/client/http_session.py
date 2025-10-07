import requests
import typing

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from bizone_ti import setup


class HttpSessionMixin:

    def __init__(self, headers: typing.Union[dict, None] = None) -> None:
        self.session = self.get_session(headers)

    def get_session(self,
                    headers: typing.Union[dict, None] = None
                    ) -> requests.Session:
        retries = Retry(
            total=setup.TIHTTPSessionConfig.RETRY_TIMES,
            backoff_factor=setup.TIHTTPSessionConfig.BACKOFF_FACTOR,
            status_forcelist=setup.TIHTTPSessionConfig.STATUS_FORCELIST,
            allowed_methods=False
        )
        session = requests.Session()

        if headers:
            session.headers = headers

        session.mount("https://", HTTPAdapter(max_retries=retries))
        session.mount("http://", HTTPAdapter(max_retries=retries))

        return session
