from __future__ import annotations
from typing import TYPE_CHECKING

import dataclasses
import logging
import typing


if TYPE_CHECKING:
    from bizone_ti.typings.abstract_entities import GeneralEntities


logger = logging.getLogger(__name__)


@dataclasses.dataclass
class ResponseRejectionObj:
    _: dataclasses.KW_ONLY
    id: str = dataclasses.field(default='')
    source: str = dataclasses.field(default='')
    value: str = dataclasses.field(default='')
    field: str = dataclasses.field(default='')
    fieldValue: str = dataclasses.field(default='')  # noqa: disable=N815
    reason: str = dataclasses.field(default='')
    message: str = dataclasses.field(default='')


@dataclasses.dataclass
class ResponseExistObj:
    _: dataclasses.KW_ONLY
    id: str = dataclasses.field(default='')
    entity: str = dataclasses.field(default='')
    value: str = dataclasses.field(default='')
    data: str = dataclasses.field(default='')
    common_id: str = dataclasses.field(default='')
    state: str = dataclasses.field(default='')


class Response:
    def __init__(self,
                 ti_object: GeneralEntities,
                 response: typing.Union[str, dict],
                 status_code: int,
                 convert_2_ti_object: bool = True) -> None:
        self._success = ()
        self._exists = ()
        self._rejections = ()
        self._status_code = status_code
        self._ti_object = ti_object
        self.raw_response = response
        self._2_ti_obj = convert_2_ti_object

        self.success = response
        self.rejections = response
        self.exists = response

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def exists(self) -> typing.Union[list[dict], None]:
        return self._exists

    @property
    def success(self
                ) -> typing.Union[list[dict], list[GeneralEntities], None]:
        return self._success

    @property
    def rejections(self) -> typing.Union[list[dict], None]:
        return self._rejections

    @exists.setter
    def exists(self, data: list[dict]) -> None:
        if "exists" not in data:
            return

        if not self._2_ti_obj:
            self._exists = tuple(data["exists"])
            return

        try:
            self._exists = tuple(
                ResponseExistObj(**exist)
                for exist in data["exists"])
        except (TypeError, Exception) as err:
            logger.exception(err)
            self._exists = tuple(data["exists"])

    @success.setter
    def success(self, data: list[dict]) -> None:
        if "id" in data:
            self._success = (data["id"],)
            return

        if "all_data" not in data:
            return

        if not self._2_ti_obj:
            self._success = tuple(data["all_data"])
            return

        self._success = tuple(
            self._ti_object.from_ti(raw_ioc['entity'],
                                    raw_ioc,
                                    skip_mismatched_types=True)
            for raw_ioc in data["all_data"]
        )

    @rejections.setter
    def rejections(self, data: list[dict]) -> None:
        if "rejections" not in data:
            return

        if not self._2_ti_obj:
            self._rejections = tuple(data["rejections"])
            return

        try:
            self._rejections = tuple(
                ResponseRejectionObj(**rejected)
                for rejected in data["rejections"]
            )
        except (TypeError, Exception) as err:
            logger.exception(err)
            self._rejections = tuple(data["rejections"])
