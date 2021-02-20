from dataclasses import dataclass

from .base_args import BaseArgs


@dataclass
class SuggestArgs(BaseArgs):
    """
    联想词 API

    :doc https://www.zhetaoke.com/user/extend/extend_lingquan_suggest.aspx
    """

    @staticmethod
    def base_url() -> str:
        return "https://api.zhetaoke.com:10001/api/api_suggest.ashx"

    content: str
