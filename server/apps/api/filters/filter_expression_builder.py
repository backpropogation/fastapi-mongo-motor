from abc import ABC, abstractmethod


class FilterExpressionBuilder(ABC):
    @abstractmethod
    def _get_query_filter_expression(self):
        raise NotImplementedError()

    @property
    def filter_expression(self) -> dict:
        return self._get_query_filter_expression()
