from dataclasses import dataclass
from typing import Optional

from .base_args import BaseArgs


@dataclass
class TMallShangPinArgs(BaseArgs):
    """
    天猫商品API：返回天猫商品列表，返回佣金≥15%，动态描述分≥4.6的商品列表。

    :doc https://www.zhetaoke.com/user/extend/extend_lingquan_tmall.aspx
    """

    @staticmethod
    def base_url():
        return "https://api.zhetaoke.com:10001/api/api_all.ashx"

    page: int = 1
    page_size: int = 20
    sort: str = "new"
    cid: Optional[int] = None

    tj: str = "tmall"
