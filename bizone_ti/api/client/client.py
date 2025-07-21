import typing

from bizone_ti import setup
from bizone_ti.api.client import base_client
from bizone_ti.api.client import query_builder


class ApiClient(base_client.BaseAPIClient):

    def __init__(self, headers: typing.Union[dict, None] = None) -> None:
        self.build_params: dict = (
            query_builder.ApiQueryBuilder().build_query_params)

        super().__init__(headers=headers)

    def get(
       self,
       uri: str,
       headers: typing.Union[dict, None] = None,
       params: typing.Union[dict, None] = None,
       **kwargs) -> tuple[int, typing.Union[str, dict]]:
        headers = headers or {
            "Authorization": f"Bearer {setup.TILibConfig.API_KEY}"}

        return super().get(
            uri,
            headers=headers,
            params=self.build_params(params),
            **kwargs
        )

    def post(
       self,
       uri: str,
       headers: typing.Union[dict, None] = None,
       params: typing.Union[dict, None] = None,
       payload: typing.Union[dict, None] = None,
       **kwargs) -> tuple[int, typing.Union[str, dict]]:
        headers = headers or {
            "Authorization": f"Bearer {setup.TILibConfig.API_KEY}"}

        return super().post(
            uri,
            headers=headers,
            params=self.build_params(params),
            json=payload,
            **kwargs
        )

    def patch(
        self,
        uri: str,
        headers: typing.Union[dict, None] = None,
        params: typing.Union[dict, None] = None,
        payload: typing.Union[dict, None] = None,
        **kwargs
    ):
        headers = headers or {
            "Authorization": f"Bearer {setup.TILibConfig.API_KEY}"}

        return super().patch(
            uri,
            headers=headers,
            params=self.build_params(params),
            json=payload,
            **kwargs
        )

    def put(
        self,
        uri: str,
        headers: typing.Union[dict, None] = None,
        params: typing.Union[dict, None] = None,
        payload: typing.Union[dict, None] = None,
        **kwargs
    ):
        headers = headers or {
            "Authorization": f"Bearer {setup.TILibConfig.API_KEY}"}

        return super().put(
            uri,
            headers=headers,
            params=self.build_params(params),
            json=payload,
            **kwargs
        )

    def delete(
        self,
        uri: str,
        headers: typing.Union[dict, None] = None,
        params: typing.Union[dict, None] = None,
        payload: typing.Union[dict, None] = None,
        **kwargs
    ) -> tuple[int, typing.Union[dict, str]]:
        headers = headers or {
            "Authorization": f"Bearer {setup.TILibConfig.API_KEY}"}

        return super().delete(
            uri,
            headers=headers,
            params=self.build_params(params),
            json=payload,
            **kwargs
        )
