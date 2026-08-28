import logging
import typing

from bizone_ti import setup


logger = logging.getLogger(f"{__name__}")


class ApiWrappersMixin:
    @staticmethod
    def update_session_configuration(func: typing.Callable) -> typing.Callable:
        def wrapper(self, *args, **kwargs):
            if setup.TIHTTPSessionConfig.HTTP_PROXY:
                self.session.proxies.update(
                    {'http': setup.TIHTTPSessionConfig.HTTP_PROXY})
            if setup.TIHTTPSessionConfig.HTTPS_PROXY:
                self.session.proxies.update(
                    {'https': setup.TIHTTPSessionConfig.HTTPS_PROXY})

            adapter_https = self.session.adapters.get('https://')
            if adapter_https:
                adapter_https.max_retries.total = (
                    setup.TIHTTPSessionConfig.RETRY_TIMES)
                adapter_https.max_retries.backoff_factor = (
                    setup.TIHTTPSessionConfig.BACKOFF_FACTOR)
                adapter_https.max_retries.status_forcelist = (
                    setup.TIHTTPSessionConfig.STATUS_FORCELIST)

            adapter_http = self.session.adapters.get('http://')
            if adapter_http:
                adapter_http.max_retries.total = (
                    setup.TIHTTPSessionConfig.RETRY_TIMES)
                adapter_http.max_retries.backoff_factor = (
                    setup.TIHTTPSessionConfig.BACKOFF_FACTOR)
                adapter_http.max_retries.status_forcelist = (
                    setup.TIHTTPSessionConfig.STATUS_FORCELIST)

            return func(self, *args, **kwargs)
        return wrapper
