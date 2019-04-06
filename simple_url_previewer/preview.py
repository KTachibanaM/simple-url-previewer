import abc
from typing import NamedTuple, List
from urllib.parse import urlparse, ParseResult


class PreviewError(ValueError):
    def __init__(self, message: str):
        super(PreviewError, self).__init__()
        self.message = message


class Preview(NamedTuple):
    title: str
    images: List[str]
    digest: str


class SitePreviewer(abc.ABC):
    @abc.abstractmethod
    def identify(self, parse_result: ParseResult) -> bool:
        pass

    @abc.abstractmethod
    def preview(self, parse_result: ParseResult) -> Preview:
        pass


class Previewer(object):
    def __init__(self, site_previewers: List[SitePreviewer], fallback_site_previewer: SitePreviewer):
        self.site_previewers = site_previewers
        self.fallback_site_previewer = fallback_site_previewer

    def preview(self, url: str) -> Preview:
        parse_result = urlparse(url)  # type: ParseResult
        for site_previewer in self.site_previewers:
            if site_previewer.identify(parse_result):
                return site_previewer.preview(parse_result)
        return self.fallback_site_previewer.preview(parse_result)
