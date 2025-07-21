from __future__ import annotations
from typing import TYPE_CHECKING
import logging
import typing

from bizone_ti.api import response as ti_response

from bizone_ti.managers import base

if TYPE_CHECKING:
    from bizone_ti.entities import (
        IoCFQDNEntity,
        IoCIPv4Entity,
        IoCURLEntity,
        IoCFileEntity,
        IoCIPv6Entity,
    )


logger = logging.getLogger(__name__)


class IoCObjectsManager(base.BaseObjectPropertyManager):

    def count(self, **kwargs) -> int:
        response = self.manager.count(
            resource=self.resource,
            **kwargs,
        )
        return response["counter"]

    def exist(self,
              sources: list[str] = None,
              values: list[str] = None,
              return_absent: bool = False,
              removed_filter: str = "not-removed"
              ) -> list[str]:
        """This method uses for getting one element from TI by string.

        Args:
            sources (list[str], optional): List of sources to check.
            Defaults to None.
            values (list[str], optional): List of IOC values to check.
            Defaults to None.
            return_absent (bool, optional):
            Return absent IOCs in the response.
            Defaults to False.
            removed_filter (str, optional): Filter by IOC status.
            Defaults to "not-removed".
            Possible values : "all", "removed", "not-removed"
        Returns:
            list[str]|None
        """
        response = self.manager.exist(
            resource=self.resource,
            payload={
                "sources": sources,
                "values": values,
                "return_absent": return_absent,
                "removed_filter": removed_filter
            }
        )

        return response.get('values', [])

    def getone(
        self,
        common_id: str = None,
        v: str = None,
        ss: str = None,
        s: str = None,
        category: list[str] = None,
        sources: list[str] = None,
        confidence: int = None,
        severity: int = None,
        tags: list[str] = None,
        download_from: int = None,
        download_to: int = None,
        limit: int = None,
        cursor: str = None,
        sort: str = "asc",
        removed_filter: str = "not-removed",
        false_positive: bool = False,
        ignore_timeout: bool = True,
        other_sources: bool = True
    ) -> typing.Union[
        IoCFQDNEntity,
        IoCIPv4Entity,
        IoCFileEntity,
        IoCIPv6Entity,
        IoCURLEntity,
        None
    ]:
        """This method uses for getting one element from TI by string.

        Args:
            common_id (str, optional): The IoC ID parameter in TI.
            v (str, optional): Search by string. Defaults to None.
            ss (str, optional): Search by substring.
            Defaults to None.
            s (str, optional): Search by string in
            several fields depends on the IoC type. Defaults to None.
            category (list[str], optional): _description_. Defaults to None.
            sources (list[str], optional): _description_. Defaults to None.
            confidence (int, optional): _description_. Defaults to None.
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
            false_positive (bool, optional): _description_. Defaults to False.
            ignore_timeout (bool, optional): _description_. Defaults to True.
            other_sources (bool, optional): _description_. Defaults to True.
            Defaults to None.
        Returns:
            IoCFQDNEntity|IoCIPv4Entity|IoCFileEntity|
            IoCIPv6Entity|IoCURLEntity|None
        """
        query_params = {
            "v": v,
            "s": s,
            "ss": ss,
            "ignore-timeout": ignore_timeout,
            "false_positive": false_positive,
            "from": download_from,
            "to": download_to,
            "removed-filter": removed_filter,
            "sort": sort,
            "category": category,
            "severity": severity,
            "sources": sources,
            "tags": tags,
            "confidence": confidence,
            "limit": limit,
            "other-sources": other_sources,
            "cursor": cursor,
        }
        response = super().getone(query_params, url_path=common_id)

        if "all_data" in response and len(response["all_data"]) > 0:
            logger.warning('Get more than one response')
            response = response["all_data"][0]

        return (self.ti_object.from_ti(self.entity_type, response)
                if len(response.get("data", [])) > 0
                else None)

    def get(
        self,
        common_id: str = None,
        v: str = None,
        ss: str = None,
        s: str = None,
        category: list[str] = None,
        sources: list[str] = None,
        confidence: int = None,
        severity: int = None,
        tags: list[str] = None,
        download_from: int = None,
        download_to: int = None,
        limit: int = None,
        cursor: str = None,
        sort: str = "asc",
        removed_filter: str = "not-removed",
        false_positive: bool = False,
        ignore_timeout: bool = True,
        other_sources: bool = True
    ) -> ti_response.ResponseGenerator:
        """This method uses for getting collection of elements from TI.

        Args:
            common_id (str, optional): The IoC ID parameter in TI.
            v (str, optional): Search by string. Defaults to None.
            ss (str, optional): Search by substring.
            Defaults to None.
            s (str, optional): Search by string in
            several fields depends on the IoC type. Defaults to None.
            category (list[str], optional): _description_. Defaults to None.
            sources (list[str], optional): _description_. Defaults to None.
            confidence (int, optional): _description_. Defaults to None.
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
            false_positive (bool, optional): _description_. Defaults to False.
            ignore_timeout (bool, optional): _description_. Defaults to True.
            other_sources (bool, optional): _description_. Defaults to True.
        Returns:
            _type_: ResponseGenerator
        """
        query_params = {
            "v": v,
            "s": s,
            "ss": ss,
            "ignore-timeout": ignore_timeout,
            "false_positive": false_positive,
            "from": download_from,
            "to": download_to,
            "removed-filter": removed_filter,
            "sort": sort,
            "category": category,
            "severity": severity,
            "sources": sources,
            "tags": tags,
            "confidence": confidence,
            "limit": limit,
            "other-sources": other_sources,
            "cursor": cursor,
        }

        return super().get(
            url_path=common_id,
            raw_responses=(common_id is not None or
                           query_params.get('v') is not None),
            query_params=query_params,
        )

    def add(
        self,
        data: typing.Union[list[dict], None] = None,
        take_screen: bool = True,
        return_result: bool = True,
        rewrite: bool = False,
        convert_2_ti_object=True,
    ) -> ti_response.Response:

        query_params = {
            "take-screen": take_screen,
            "return-result": return_result,
            "rewrite": rewrite,
        }

        return super().add(
            data=data,
            query_params=query_params,
            convert_2_ti_object=convert_2_ti_object,
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

    def linked(
        self,
        common_id: str,
        cursor: str = None,
        limit: int = None,
        removed: bool = False,
    ) -> ti_response.ResponseGenerator:  # noqa W0221
        return super().linked(
            entity_id=common_id, cursor=cursor, limit=limit, removed=removed
        )

    def make_link(
        self,
        common_id: str,
        object_ids: list[str],
    ) -> ti_response.Response:
        return super().make_link(
            entity_id=common_id,
            object_ids=object_ids,
        )

    def unlink(
        self,
        common_id: str,
        object_ids: list[str],
    ) -> ti_response.Response:
        return super().unlink(
            entity_id=common_id,
            object_ids=object_ids,
        )
