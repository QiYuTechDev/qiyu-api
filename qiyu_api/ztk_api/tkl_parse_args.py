from pydantic import Field

from .base_args import BaseArgs


class TKLParseArgs(BaseArgs):
    @staticmethod
    def base_url() -> str:
        return "https://api.zhetaoke.com:10001/api/open_shangpin_id.ashx"

    content: str = Field(..., title="淘口令内容")

    sid: str = Field(..., title="SID")

    typ: int = Field(1, alias="type")
