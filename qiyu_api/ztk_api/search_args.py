from dataclasses import dataclass
from typing import Optional

from .base_args import BaseArgs


@dataclass
class SearchArgs(BaseArgs):
    """
    全网搜索商品

    :doc https://www.zhetaoke.com/user/extend/extend_lingquan_keywords.aspx
    """

    @staticmethod
    def base_url() -> str:
        return "https://api.zhetaoke.com:10003/api/api_quanwang.ashx"

    q: str

    page: int = 1
    page_size: int = 20
    sort: str = "new"

    youquan: Optional[int] = None
    haiwai: Optional[int] = None
    haoping: Optional[int] = None
    tj: Optional[str] = None
    itemloc: Optional[str] = None
    cat: Optional[str] = None
    start_tk_rate: Optional[str] = None
    end_tk_rate: Optional[str] = None
    start_price: Optional[str] = None
    end_price: Optional[str] = None
    # 过滤值
    # 值为0：不过滤，
    # 值为1：轻度过滤，
    # 值为2：中度过滤，
    # 强烈推荐值为2。
    type: int = 2
