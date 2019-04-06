import requests
from urllib.parse import ParseResult
from bs4 import BeautifulSoup
from . import Preview, SitePreviewer


class FallbackSitePreviewer(SitePreviewer):
    def identify(self, parse_result: ParseResult) -> bool:
        return True

    def preview(self, parse_result: ParseResult) -> Preview:
        full_url = parse_result.geturl()
        html_doc = requests.get(full_url).content
        bs = BeautifulSoup(html_doc, "html.parser")
        images = list(map(lambda img: self.sanitize_src(parse_result, img['src']), bs.find_all("img")))
        return Preview(
            title=bs.title.text,
            images=images,
            digest=''  # todo
        )

    def sanitize_src(self, parse_result: ParseResult, src: str) -> str:
        if src.startswith('/'):
            # looks like using relative path
            return f"{parse_result.scheme}://{parse_result.netloc}{src}"
        return src
