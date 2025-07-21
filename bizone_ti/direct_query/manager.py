from __future__ import annotations
import typing

from bizone_ti.api import client
from bizone_ti.direct_query import validators


class DirectQueryManager:

    def __new__(cls: DirectQueryManager) -> typing.Self:
        if not hasattr(cls, "instance"):
            cls.instance: typing.Self = super(DirectQueryManager, cls).__new__(
                cls)
        return cls.instance

    def __init__(self) -> None:
        self.api_client: client.BaseAPIClient = client.BaseAPIClient()

    @validators.header_checker_wrapper
    @validators.url_checker_wrapper
    def get(
       self,
       uri: str,
       headers: typing.Union[dict, None] = None,
       params: typing.Union[dict, None] = None,
       **kwargs
       ) -> typing.Tuple[int, typing.Union[str, dict]]:
        return self.api_client.get(
            uri,
            headers=headers,
            params=params,
            **kwargs
        )

    @validators.header_checker_wrapper
    @validators.url_checker_wrapper
    def post(
       self,
       uri: str,
       params: typing.Union[dict, None] = None,
       headers: typing.Union[dict, None] = None,
       json: typing.Union[dict, None] = None,
       **kwargs
       ) -> typing.Tuple[int, typing.Union[str, dict]]:
        return self.api_client.post(
            uri,
            headers=headers,
            params=params,
            json=json,
            **kwargs
        )

    @validators.header_checker_wrapper
    @validators.url_checker_wrapper
    def patch(
       self,
       uri: str,
       params: typing.Union[dict, None] = None,
       headers: typing.Union[dict, None] = None,
       json: typing.Union[dict, None] = None,
       **kwargs
       ) -> typing.Tuple[int, typing.Union[str, dict]]:
        return self.api_client.patch(
            uri,
            headers=headers,
            params=params,
            json=json,
            **kwargs
        )

    @validators.header_checker_wrapper
    @validators.url_checker_wrapper
    def put(
       self,
       uri: str,
       params: typing.Union[dict, None] = None,
       headers: typing.Union[dict, None] = None,
       json: typing.Union[dict, None] = None,
       **kwargs
       ) -> typing.Tuple[int, typing.Union[str, dict]]:
        return self.api_client.put(
            uri,
            headers=headers,
            params=params,
            json=json,
            **kwargs
        )

    @validators.header_checker_wrapper
    @validators.url_checker_wrapper
    def delete(
       self,
       uri: str,
       params: typing.Union[dict, None] = None,
       headers: typing.Union[dict, None] = None,
       json: typing.Union[dict, None] = None,
       **kwargs
       ) -> typing.Tuple[int, typing.Union[str, dict]]:
        return self.api_client.delete(
            uri,
            headers=headers,
            params=params,
            json=json,
            **kwargs
        )
