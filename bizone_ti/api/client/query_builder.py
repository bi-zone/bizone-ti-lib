import collections
import functools


class ApiQueryBuilder:
    def __init__(self) -> None:
        self.PARAM_2_FORMAT_MAP: dict = {
            "category": functools.partial(self._get_formatted_filter,
                                          "category"),
            "sources": functools.partial(self._get_formatted_filter,
                                         "source"),
            "tags": functools.partial(self._get_formatted_filter,
                                      "tags"),
            "confidence": lambda confidence_level: (
                f"confidence>={confidence_level}"),
            "false_positive": lambda fp: "" if fp else "!false_positive",
            "motivation_type": functools.partial(self._get_formatted_filter,
                                                 "motivation_type"),
            "industry": functools.partial(self._get_formatted_filter,
                                          "industry"),
        }

    @staticmethod
    def _get_formatted_filter(filter_type: str, filters: list) -> str:
        filter_list = [f'{filter_type}=="{filter}"' for filter in filters]
        return f"({'|'.join(filter_list)})" if filter_list else None

    def build_query_params(self, query_params: dict) -> dict:
        if query_params is None:
            return query_params

        builded_params = collections.defaultdict(list)

        for q_name, q_value in query_params.items():
            if q_value is None:
                continue

            if q_name not in self.PARAM_2_FORMAT_MAP:
                if q_name in ('from', 'to'):
                    builded_params[q_name] = int(q_value)
                else:
                    builded_params[q_name] = q_value
                continue

            formatted_filter = self.PARAM_2_FORMAT_MAP[q_name](q_value)
            if formatted_filter:
                builded_params["q"].append(formatted_filter)

        if len(builded_params.get("q", [])) > 1:
            builded_params["q"] = "&".join(builded_params["q"])
            builded_params["q"] = f'({builded_params["q"]})'

        return builded_params
