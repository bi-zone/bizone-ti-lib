import functools
import typing

from bizone_ti import setup
from bizone_ti.api import client


class Request:
    def __init__(self) -> None:
        self.api_client: client.ApiClient = client.ApiClient()

    @staticmethod
    def build_uri(*args: tuple[str]) -> str:
        return setup.TILibConfig.TI_URL + "/".join(filter(lambda i: i, args))

    def get_resource(
        self,
        resource: str,
        url_path: typing.Union[str, None] = None,
        params: typing.Union[dict, None] = None
    ) -> typing.Union[dict, str]:
        _, response = self.api_client.get(
            self.build_uri(resource, url_path),
            params=params
        )
        return response

    def post_resource(
        self,
        resource: str,
        url_path: typing.Union[str, None] = None,
        params: typing.Union[dict, None] = None,
        payload: typing.Union[dict, None] = None
    ) -> tuple[int, typing.Union[dict, str]]:
        status_code, response = self.api_client.post(
            self.build_uri(resource, url_path),
            params=params,
            payload=payload
        )
        return status_code, response

    def patch_resource(
        self,
        resource: str,
        url_path: typing.Union[str, None] = None,
        params: typing.Union[dict, None] = None,
        payload: typing.Union[dict, None] = None
    ) -> tuple[int, typing.Union[dict, str]]:
        status_code, response = self.api_client.patch(
            self.build_uri(resource, url_path),
            params=params,
            payload=payload
        )
        return status_code, response

    def delete_resource(
        self,
        resource: str,
        url_path: typing.Union[str, None] = None,
        payload: typing.Union[dict, None] = None
    ) -> tuple[int, typing.Union[dict, str]]:
        status_code, response = self.api_client.delete(
            self.build_uri(resource, url_path),
            payload=payload,
        )
        return status_code, response

    def get_hook(
        self,
        resource: str,
        url_path: typing.Union[str, None] = None,
    ) -> functools.partial:
        return functools.partial(
            self.api_client.get,
            self.build_uri(resource, url_path),
        )

    def execute_hook(
        self,
        request_hook: functools.partial,
        params: typing.Union[dict, None],
        pages_to_download: int = 1,
        raw_responses: bool = False
    ) -> tuple[list, str]:
        part_response = []
        while pages_to_download:
            _, page = request_hook(
                params=params,
                verify=False
            )

            if raw_responses:
                part_response.append(page)
            else:
                response = page.get("all_data", []) or page.get("data", [])
                if len(response) == 0:
                    break

                if isinstance(response, list):
                    part_response.extend(response)
                elif isinstance(response, dict):
                    for _, entities_value in response.items():
                        for _, v in entities_value.items():
                            if len(v):
                                part_response.extend(v)
                else:
                    raise Exception()

            if page.get("next_cursor") is None:
                break

            if (params.get("cursor") and
               page.get("next_cursor") == params.get("cursor")):
                break

            params["cursor"] = page["next_cursor"]
            pages_to_download -= 1

        return part_response, page.get("next_cursor")
