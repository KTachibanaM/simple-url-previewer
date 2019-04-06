from typing import Optional
from urllib.parse import ParseResult, parse_qs
from simple_url_previewer import Preview
from . import SitePreviewer, PreviewError


class PixivPreviewer(SitePreviewer):
    def identify(self, parse_result: ParseResult) -> bool:
        if "pixiv.net" not in parse_result.netloc or not parse_result.query:
            return False
        if not self.get_illust_id(parse_result.query):
            return False
        return True

    def preview(self, parse_result: ParseResult) -> Preview:
        illust_id = self.get_illust_id(parse_result.query)


    def get_illust_id(self, qs: str) -> Optional[str]:
        parsed_query = parse_qs(qs)
        if 'illust_id' not in parsed_query:
            return None
        if len(parsed_query['illust_id']) != 1:
            return None  # todo: warning here?
        return parsed_query['illust_id'][0]
