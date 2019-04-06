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
        images = []
        for img in bs.find_all("img"):
            if "src" in img.attrs:
                src = img["src"]
                if src.startswith('/'):
                    # looks like using relative path
                    src = f"{parse_result.scheme}://{parse_result.netloc}{src}"
                images.append(src)
        return Preview(
            title=bs.title.text,
            images=images,
            digest=''  # todo
        )
