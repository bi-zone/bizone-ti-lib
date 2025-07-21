from __future__ import annotations

import logging
import typing

from bizone_ti.api import response as ti_response
from bizone_ti.managers import base

if typing.TYPE_CHECKING:
    from bizone_ti.entities import (
        GroupAdversaryEntity,
        GroupGeneralEntity,
        GroupToolEntity,
        GroupMalwareEntity,
        GroupVulnerabilityEntity,)


logger = logging.getLogger(__name__)


class GroupObjectsManager(base.BaseObjectPropertyManager):
    def getone(
        self,
        group_id: str = None,
        v: str = None,
        ss: str = None,
        s: str = None,
        category: list[str] = None,
        sources: list[str] = None,
        severity: int = None,
        tags: list[str] = None,
        download_from: int = None,
        download_to: int = None,
        limit: int = None,
        cursor: str = None,
        sort: str = "asc",
        removed_filter: str = "not-removed",
        ignore_timeout: bool = True,
        other_sources: bool = True
    ) -> typing.Union[
        GroupAdversaryEntity,
        GroupGeneralEntity,
        GroupToolEntity,
        GroupMalwareEntity,
        GroupVulnerabilityEntity,
        None
    ]:
        """This method uses for getting one element from TI by string.

        Args:
            group_id (str, optional): Search by group id.
            Defaults to None.
            v (str, optional): Search by string.
            Defaults to None.
            ss (str, optional): Search by substring.
            Defaults to None.
            s (str, optional): Search by string in several
            fields depends on the group type. Defaults to None.
            category (list[str], optional): _description_. Defaults to None.
            sources (list[str], optional): _description_. Defaults to None.
            severity (int, optional): _description_. Defaults to None.
            tags (list[str], optional): _description_. Defaults to None.
            download_from (int, optional): _description_. Defaults to None.
            download_to (int, optional): _description_. Defaults to None.
            limit (int, optional): _description_. Defaults to None.
            cursor (str, optional): _description_. Defaults to None.
            sort (str, optional): _description_. Defaults to "asc".
            removed_filter (str, optional): _description_.
                    Defaults to "not-removed". Possible values  "not-removed",
                    "removed", "all".
            ignore_timeout (bool, optional): _description_. Defaults to True.
            other_sources (bool, optional): Use other sources in response.
            Defaults to True.
        Returns:
            GroupAdversaryEntity|GroupGeneralEntity|GroupToolEntity|
            GroupMalwareEntity|GroupVulnerabilityEntity|None
        """

        query_params = {
            "v": v,
            "s": s,
            "ss": ss,
            "ignore-timeout": ignore_timeout,
            "from": download_from,
            "to": download_to,
            "removed-filter": removed_filter,
            "sort": sort,
            "category": category,
            "severity": severity,
            "sources": sources,
            "tags": tags,
            "limit": limit,
            "other-sources": other_sources,
            "cursor": cursor,
        }

        response = super().getone(query_params, url_path=group_id)
        if "data" in response:
            if len(response["data"]) == 0:
                return None
            elif len(response["data"]) > 1:
                logger.warning('Get more than one response')
                return self.ti_object.from_ti(
                    self.entity_type, response["data"][0])

        return self.ti_object.from_ti(
            self.entity_type, response) if response else None

    def get(
        self,
        group_id: str = None,
        v: str = None,
        ss: str = None,
        s: str = None,
        category: list[str] = None,
        sources: list[str] = None,
        severity: int = None,
        tags: list[str] = None,
        download_from: int = None,
        download_to: int = None,
        limit: int = None,
        cursor: str = None,
        sort: str = "asc",
        removed_filter: str = "not-removed",
        ignore_timeout: bool = True,
        other_sources: bool = True
    ) -> ti_response.ResponseGenerator:
        """This method uses for getting one element from TI by string.

        Args:
            group_id (str, optional): Search by group id.
            v (str, optional): Search by string. Defaults to None.
            ss (str, optional): Search by substring.
            Defaults to None.
            s (str, optional): Search by string in
            several fields depends on the group type. Defaults to None.
            category (list[str], optional): _description_. Defaults to None.
            sources (list[str], optional): _description_. Defaults to None.
            severity (int, optional): _description_. Defaults to None.
            tags (list[str], optional): _description_. Defaults to None.
            download_from (int, optional): _description_. Defaults to None.
            download_to (int, optional): _description_. Defaults to None.
            limit (int, optional): _description_. Defaults to None.
            cursor (str, optional): _description_. Defaults to None.
            sort (str, optional): _description_. Defaults to "asc".
            removed_filter (str, optional): _description_.
                    Defaults to "not-removed". Possible values  "not-removed",
                    "removed", "all".
            ignore_timeout (bool, optional): _description_. Defaults to True.
            other_sources (bool, optional): _description_. Defaults to True.
        Returns:
            _type_: _description_
        """

        query_params = {
            "v": v,
            "s": s,
            "ss": ss,
            "ignore-timeout": ignore_timeout,
            "from": download_from,
            "to": download_to,
            "removed-filter": removed_filter,
            "sort": sort,
            "category": category,
            "severity": severity,
            "sorces": sources,
            "tags": tags,
            "limit": limit,
            "other-sources": other_sources,
            "cursor": cursor,
        }

        return super().get(
            url_path=group_id,
            raw_responses=group_id is not None,
            query_params=query_params,
        )

    def add(
        self,
        data: typing.Union[dict, None] = None,
        convert_2_ti_object: bool = True
    ) -> ti_response.Response:

        query_params = {
            "take-screen": True,
            "return-result": True,
            "rewrite": False,
        }

        return super().add(
            data=data,
            query_params=query_params,
            url_path="",
            convert_2_ti_object=convert_2_ti_object,
        )

    def linked(
        self,
        group_id: str,
        cursor: str = None,
        limit: int = None,
        removed: bool = False,
    ) -> ti_response.ResponseGenerator:
        return super().linked(
            entity_id=group_id,
            cursor=cursor,
            limit=limit,
            removed=removed
        )

    def delete(self, group_id: str) -> ti_response.Response:
        return super().delete(resource=self.resource, url_path=group_id)

    def make_link(
        self,
        group_id: str,
        object_ids: list[str],
    ) -> ti_response.Response:
        return super().make_link(
            entity_id=group_id,
            object_ids=object_ids,
        )

    def unlink(
        self,
        group_id: str,
        object_ids: list[str],
    ) -> ti_response.Response:
        return super().unlink(
            entity_id=group_id,
            object_ids=object_ids,
        )
