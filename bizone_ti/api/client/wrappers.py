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
            return func(self, *args, **kwargs)
        return wrapper
