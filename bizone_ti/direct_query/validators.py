import logging
import typing

from urllib.parse import urlparse

from bizone_ti import exceptions
from bizone_ti.direct_query import settings


logger = logging.getLogger(f"{__name__}")


def has_different_domain(uri):
    current_domain = urlparse(uri)
    return (settings.DirectQuerySettingsSelector.TI_DOMAIN ==
            current_domain.netloc)


def url_checker_wrapper(func: typing.Callable) -> typing.Callable:
    def wrapper(self, *args, **kwargs):
        uri = args[0] if len(args) > 0 else kwargs.get('uri')

        if uri is None:
            raise exceptions.NotEnoughValues("Expected uri, found nothing")

        # setup DirectQuerySettingsSelector
        if settings.DirectQuerySettingsSelector.TI_URL is None:
            settings.DirectQuerySettingsSelector.select()

        if not has_different_domain(uri):
            logger.warning("URI %s has different domain "
                           "than expected %s."
                           "Is that correct?",
                           uri, settings.DirectQuerySettingsSelector.TI_DOMAIN)

        return func(self, *args, **kwargs)

    return wrapper


def header_checker_wrapper(func: typing.Callable) -> typing.Callable:
    def wrapper(self, *args, **kwargs):
        # setup DirectQuerySettingsSelector
        if settings.DirectQuerySettingsSelector.API_KEY is None:
            settings.DirectQuerySettingsSelector.select()

        if kwargs.get('headers') is None:
            kwargs['headers'] = {
                "Authorization": (
                    "Bearer "
                    f"{settings.DirectQuerySettingsSelector.API_KEY}")
                }

        return func(self, *args, **kwargs)

    return wrapper
