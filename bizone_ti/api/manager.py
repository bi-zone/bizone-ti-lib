from __future__ import annotations

import typing

from bizone_ti.api import request
from bizone_ti.api import response as ti_reponse

from bizone_ti.typings.abstract_entities import GeneralEntities


class ApiManager:
    """Singleton"""

    def __new__(cls: ApiManager) -> typing.Self:
        if not hasattr(cls, "instance"):
            cls.instance: typing.Self = super(ApiManager, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.request: request.Request = request.Request()

    def count(self,
              resource: str,
              params: typing.Union[dict, None] = None
              ) -> typing.Union[str, dict]:
        return self.request.get_resource(resource, "count", params)

    def exist(self,
              resource: str,
              payload: dict,
              url_path: str = "exist",
              params: typing.Union[dict, None] = None,
              ) -> typing.Union[str, dict]:
        _, response = self.request.post_resource(
            resource, url_path, params, payload)
        return response

    def getone(self,
               resource: str,
               url_path: typing.Union[str, None] = None,
               params: typing.Union[dict, None] = None
               ) -> typing.Union[str, dict]:
        return self.request.get_resource(resource, url_path, params)

    def getall(
        self,
        resource: str,
        entity_type: str,
        url_path: typing.Union[str, None] = None,
        raw_responses: bool = False,
        params: typing.Union[dict, None] = None,
        convert_to_type: typing.Union[GeneralEntities, None] = None
       ) -> ti_reponse.ResponseGenerator:
        req_hook = self.request.get_hook(resource, url_path)

        return ti_reponse.ResponseGenerator(
            request_hook=req_hook,
            raw_responses=raw_responses,
            entity_type=entity_type,
            params=params,
            convert_to_type=convert_to_type)

    def add(
        self,
        resource: str,
        params: typing.Union[dict, None],
        payload: dict,
        ti_object: GeneralEntities,
        url_path: str = "add",
        convert_2_ti_object: bool = True,
    ) -> ti_reponse.Response:
        status_code, response = self.request.post_resource(
            resource, url_path, params, payload
        )

        return ti_reponse.Response(
            ti_object=ti_object,
            response=response,
            status_code=status_code,
            convert_2_ti_object=convert_2_ti_object,
        )

    def delete(self,
               resource: str,
               payload: typing.Union[dict, None] = None,
               url_path: str = "delete") -> ti_reponse.Response:
        status_code, response = self.request.delete_resource(
            resource, url_path, payload)

        return ti_reponse.Response(
            ti_object=None,
            response=response,
            status_code=status_code,
            convert_2_ti_object=False,
        )

    def manage_link(
        self,
        entity_id: str,
        resource: str,
        payload: dict,
        params: dict,
    ) -> ti_reponse.Response:

        status_code, response = self.request.patch_resource(
            resource=resource,
            url_path=f"{entity_id}/linked",
            params=params,
            payload=payload)

        return ti_reponse.Response(
            ti_object=None,
            response=response,
            status_code=status_code,
            convert_2_ti_object=False,
        )

    def linked(self,
               resource: str,
               entity_id: str,
               entity_type: str,
               params: dict) -> ti_reponse.ResponseGenerator:
        req_hook = self.request.get_hook(resource, f"{entity_id}/linked")
        return ti_reponse.ResponseGenerator(
            request_hook=req_hook,
            entity_type=entity_type,
            params=params)


class IoCApiManager(ApiManager):
    def delete(self,
               resource: str,
               payload: typing.Union[dict, None] = None,
               url_path: str = "delete") -> ti_reponse.Response:
        status_code, response = self.request.post_resource(
            resource=resource,
            url_path=url_path,
            params=None,
            payload=payload
        )

        return ti_reponse.Response(
            ti_object=None,
            response=response,
            status_code=status_code,
            convert_2_ti_object=False,
        )
