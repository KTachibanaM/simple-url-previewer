import requests
from typing import Optional
from urllib.parse import ParseResult, parse_qs
from bs4 import BeautifulSoup
from . import Preview, SitePreviewer, PreviewError


class PixivPreviewer(SitePreviewer):
    def __init__(self):
        pass

    def identify(self, parse_result: ParseResult) -> bool:
        if "pixiv.net" not in parse_result.netloc or not parse_result.query:
            return False
        if not self.get_illust_id(parse_result.query):
            return False
        return True

    def preview(self, parse_result: ParseResult) -> Preview:
        illust_id = self.get_illust_id(parse_result.query)
        html_doc = requests.get(f"https://www.pixiv.net/member_illust.php?mode=medium&illust_id={illust_id}").content
        bs = BeautifulSoup(html_doc, "html.parser")
        clickable_image = bs.find("a", {"data-title": "registerImage"})
        if not clickable_image:
            # todo: warn me as well
            raise PreviewError("pixiv: cannot find clickable image")
        img = getattr(clickable_image, "img")
        if not img:
            # todo: warn me as well
            raise PreviewError("pixiv: cannot find img in clickable image")
        img_src = img['src']
        return Preview(
            title=bs.title.text,
            images=[img_src],
            digest=''  # todo
        )

    def get_illust_id(self, qs: str) -> Optional[str]:
        parsed_query = parse_qs(qs)
        if 'illust_id' not in parsed_query:
            return None
        if len(parsed_query['illust_id']) != 1:
            return None  # todo: warning here?
        return parsed_query['illust_id'][0]
