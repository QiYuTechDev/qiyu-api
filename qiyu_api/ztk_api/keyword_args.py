from dataclasses import dataclass

from .base_args import BaseArgs


@dataclass
class KeywordArgs(BaseArgs):
    """
    关键词词典

    :doc https://www.zhetaoke.com/user/extend/extend_lingquan_guanjianci.aspx
    """

    @staticmethod
    def base_url() -> str:
        return "https://api.zhetaoke.com:10001/api/api_guanjianci.ashx"

    page: int = 1
    page_size: int = 10
    type: int = 1
