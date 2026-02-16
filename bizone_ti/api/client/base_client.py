import logging
import typing
import urllib3

from bizone_ti import setup
from bizone_ti import utils
from bizone_ti.api.client import http_session
from bizone_ti.api.client import wrappers


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


logger = logging.getLogger(f"{__name__}")


class BaseAPIClient(http_session.HttpSessionMixin):
    @wrappers.ApiWrappersMixin.update_session_configuration
    def get(self,
            url: str,
            **kwargs: dict) -> tuple[int, typing.Union[str, dict]]:
        logger.debug("GET %s kwargs %s", url, kwargs)
        response = self.session.get(url, **kwargs)
        logger.debug(
            "GET %s kwargs %s STATUS_CODE %d",
            url, kwargs, response.status_code
        )
        response.raise_for_status()
        return response.status_code, utils.try_convert_to_json(response.text)

    @wrappers.ApiWrappersMixin.update_session_configuration
    def post(self,
             url: str,
             **kwargs: dict) -> tuple[int, typing.Union[str, dict]]:
        logger.debug("POST %s kwargs %s", url, kwargs)
        response = self.session.post(url, **kwargs)
        if (response.status_code not in
           setup.TIHTTPSessionConfig.HTTP_SUCCESS_CODES):
            logger.debug(
                "POST %s kwargs %s STATUS_CODE %d response %s",
                url,
                kwargs,
                response.status_code,
                response.text,
            )

        return response.status_code, utils.try_convert_to_json(response.text)

    @wrappers.ApiWrappersMixin.update_session_configuration
    def patch(self,
              url: str,
              **kwargs: dict) -> tuple[int, typing.Union[str, dict]]:
        logger.debug("PATCH %s kwargs %s", url, kwargs)
        response = self.session.patch(url, **kwargs)
        if (response.status_code not in
           setup.TIHTTPSessionConfig.HTTP_SUCCESS_CODES):
            logger.info(
                "PATCH %s kwargs %s STATUS_CODE %d response %s",
                url,
                kwargs,
                response.status_code,
                response.text,
            )
        response.raise_for_status()
        return response.status_code, utils.try_convert_to_json(response.text)

    @wrappers.ApiWrappersMixin.update_session_configuration
    def put(self,
            url: str,
            **kwargs: dict) -> tuple[int, typing.Union[str, dict]]:
        logger.debug("PATCH %s kwargs %s", url, kwargs)
        response = self.session.put(url, **kwargs)
        if (response.status_code not in
           setup.TIHTTPSessionConfig.HTTP_SUCCESS_CODES):
            logger.info(
                "PATCH %s kwargs %s STATUS_CODE %d response %s",
                url,
                kwargs,
                response.status_code,
                response.text,
            )
        response.raise_for_status()
        return response.status_code, utils.try_convert_to_json(response.text)

    @wrappers.ApiWrappersMixin.update_session_configuration
    def delete(self,
               url: str,
               **kwargs: dict) -> tuple[int, typing.Union[str, dict]]:
        logger.debug("DELETE %s kwargs %s", url, **kwargs)
        response = self.session.delete(url, **kwargs)
        if (response.status_code not in
           setup.TIHTTPSessionConfig.HTTP_SUCCESS_CODES):
            logger.info(
                "DELETE %s STATUS_CODE %d response %s",
                url,
                response.status_code,
                response.text,
            )
        response.raise_for_status()
        return response.status_code, response.text
