from typing import NamedTuple, List
from urllib.parse import urlparse, ParseResult


class PreviewError(ValueError):
    def __init__(self, message: str):
        super(PreviewError, self).__init__()
        self.message = message


class Preview(NamedTuple):
    title: str
    image_urls: List[str]
    text_digest: str


class Previewer(object):
    def __init__(self):
        pass

    def preview(self, url: str) -> Preview:
        parse_result = urlparse(url)  # type: ParseResult
        if not parse_result.netloc:
            raise PreviewError(f"{url} does not seem to be a valid url")
        netloc = parse_result.netloc
