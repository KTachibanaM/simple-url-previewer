import abc
from urllib.parse import ParseResult
from . import Preview


class SitePreviewer(abc.ABC):
    @abc.abstractmethod
    def identify(self, parse_result: ParseResult) -> bool:
        pass

    @abc.abstractmethod
    def preview(self, parse_result: ParseResult) -> Preview:
        pass
