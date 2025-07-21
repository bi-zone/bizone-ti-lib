from __future__ import annotations
import functools
from typing import TYPE_CHECKING

import collections
import logging
import typing

from bizone_ti.api import request

if TYPE_CHECKING:
    from bizone_ti.typings.abstract_entities import GeneralEntities


logger = logging.getLogger(__name__)


class ResponseGenerator:
    """A generator which yeild information from TI"""

    MAX_CHUNK = 300
    PAGES_PER_DOWNLOAD = 10

    def __init__(
       self,
       request_hook: functools.partial,
       entity_type: typing.Union[str, None] = None,
       params: typing.Union[dict, None] = None,
       executor: typing.Union[typing.Callable, None] = None,
       raw_responses: bool = False,
       convert_to_type: typing.Union[GeneralEntities, None] = None) -> None:

        self.__processed: int = 0
        self.request_hook: functools.partial = request_hook
        # TODO do not create object here
        self.executor = executor or request.Request().execute_hook

        self.params = {} if params is None else params
        if "limit" not in self.params:
            self.params["limit"] = self.MAX_CHUNK

        self.raw_responses = raw_responses

        self.__to_type: GeneralEntities = convert_to_type
        self.__cursor: str = None
        self.__buffer: collections.deque = collections.deque()
        self._entity_type: str = entity_type

        self.__break_iteration = False

    @property
    def to_type(self) -> GeneralEntities:
        return self.__to_type

    @to_type.setter
    def to_type(self, obj):
        self.__to_type = obj

    @property
    def cursor(self) -> str:
        return self.__cursor

    @cursor.setter
    def cursor(self, new_cursor: str):
        self.__cursor = new_cursor

    @property
    def buffer(self) -> collections.deque:
        return self.__buffer

    @property
    def entity_type(self) -> str:
        return self._entity_type

    @classmethod
    def setup(cls, pages_per_download: int = 10):
        cls.PAGES_PER_DOWNLOAD = pages_per_download

    @property
    def processed(self) -> int:
        return self.__processed

    @processed.setter
    def processed(self, val: int):
        self.__processed = val

    def __iter__(self):
        return self

    def __next__(self):
        if self.__break_iteration:
            raise StopIteration

        if len(self.buffer) == 0:
            responses, cursor = self.executor(
                self.request_hook,
                self.params,
                self.PAGES_PER_DOWNLOAD,
                self.raw_responses)

            if cursor:
                if self.cursor == cursor:
                    raise StopIteration

                self.cursor = cursor
                self.params["cursor"] = cursor
            else:
                self.__break_iteration = True

            if len(responses) == 0:
                raise StopIteration

            for response in responses:
                self.buffer.append(response)

        raw_item = self.buffer.popleft()
        self.processed += 1

        if self.to_type:
            return self.to_type.from_ti(
                self.entity_type, raw_item)

        return raw_item
