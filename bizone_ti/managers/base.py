from __future__ import annotations

import typing

from bizone_ti.api import response as ti_response

if typing.TYPE_CHECKING:
    from bizone_ti.typings.api_manager import ApiManagers
    from bizone_ti.typings.abstract_entities import GeneralEntities


class BaseObjectPropertyManager:
    @property
    def manager(
        self,
    ) -> ApiManagers:
        return self.__manager__

    @property
    def ti_object(self) -> GeneralEntities:
        return self.__obj__

    def getone(self,
               query_params: dict,
               url_path: str = None
               ) -> typing.Union[str, dict]:
        return self.manager.getone(
            resource=self.resource,
            url_path=url_path,
            params=query_params,
        )

    def get(self,
            query_params: dict,
            raw_responses: bool = False,
            url_path: str = None) -> typing.Union[str, dict]:
        return self.manager.getall(
            resource=self.resource,
            url_path=url_path,
            raw_responses=raw_responses,
            entity_type=self.entity_type,
            params=query_params,
            convert_to_type=self.ti_object
        )

    def add(
        self,
        data: list[dict],
        query_params=None,
        url_path="add",
        convert_2_ti_object=True,
    ) -> ti_response.Response:

        return self.manager.add(
            resource=self.resource,
            params=query_params,
            payload=data,
            ti_object=self.ti_object,
            url_path=url_path,
            convert_2_ti_object=convert_2_ti_object,
        )

    def linked(
        self,
        entity_id: str,
        cursor: str = None,
        limit: int = None,
        removed: bool = False,
    ) -> ti_response.ResponseGenerator:
        """This method uses for getting all linked  iocs&groups
           to specified group from TI.

        Args:
            entity_id (str): _description_
            cursor (str, optional): _description_. Defaults to None.
            limit (int, optional): _description_. Defaults to None.
            removed (bool, optional): _description_. Defaults to False.

        Returns:
            object:ti_reponse.Response
        """
        query_params = {
            "limit": limit,
            "cursor": cursor,
            "removed": removed,
        }

        return self.manager.linked(
            resource=self.resource,
            entity_id=entity_id,
            entity_type=self.entity_type,
            params=query_params,
        )

    def make_link(
        self,
        entity_id: str,
        object_ids: list,
    ) -> ti_response.Response:
        payload = {
            "patch": {
                "add": object_ids,
            }
        }

        return self.manager.manage_link(
            resource=self.resource,
            entity_id=entity_id,
            payload=payload,
        )

    def unlink(
        self,
        entity_id: str,
        object_ids: list,
    ) -> ti_response.Response:
        payload = {
            "patch": {
                "remove": object_ids,
            }
        }

        return self.manager.manage_link(
            resource=self.resource,
            entity_id=entity_id,
            payload=payload,
        )

    def delete(self, **kwargs):
        return self.manager.delete(**kwargs)


class BaseIoCEntityManager(BaseObjectPropertyManager):

    def linked(
        self, cursor: str = None, limit: int = None, removed: bool = False
    ) -> ti_response.ResponseGenerator:
        return super().linked(
            entity_id=self.common_id,
            cursor=cursor,
            limit=limit,
            removed=removed
        )

    def make_link(
        self,
        object_ids: list,
    ) -> ti_response.Response:
        return super().make_link(
            entity_id=self.common_id,
            object_ids=object_ids,
        )

    def unlink(
        self,
        object_ids: list,
    ) -> ti_response.Response:
        return super().unlink(
            entity_id=self.common_id,
            object_ids=object_ids,
        )

    def delete(self, value: str, source: str
               ) -> tuple[int, typing.Union[str, dict]]:
        payload = [
            {
                "value": value,
                "source": source,
            }
        ]

        return super().delete(
            resource=self.resource,
            payload=payload,
        )


class BaseGroupEntityManager(BaseObjectPropertyManager):

    def linked(
        self, cursor: str = None, limit: int = None, removed: bool = False
    ) -> ti_response.ResponseGenerator:
        _, group_id = self.id.split(":")
        return super().linked(
            entity_id=group_id,
            cursor=cursor,
            limit=limit,
            removed=removed
        )

    def make_link(
        self,
        object_ids: list,
    ) -> ti_response.Response:
        _, group_id = self.id.split(":")
        return super().make_link(
            entity_id=group_id,
            object_ids=object_ids,
        )

    def unlink(
        self,
        object_ids: list,
    ) -> ti_response.Response:
        _, group_id = self.id.split(":")
        return super().unlink(
            entity_id=group_id,
            object_ids=object_ids,
        )
