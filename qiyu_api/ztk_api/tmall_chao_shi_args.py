from dataclasses import dataclass
from typing import Optional

from .base_args import BaseArgs


@dataclass
class TMallChaoShiArgs(BaseArgs):
    """
    天猫超市商品API：返回天猫超市商品列表，动态描述分≥4.6的商品列表，根据不同参数可返回天猫超市单件免邮商品。

    :doc https://www.zhetaoke.com/user/extend/extend_lingquan_tianmaochaoshi.aspx
    """

    @staticmethod
    def base_url():
        return "https://api.zhetaoke.com:10001/api/api_all.ashx"

    page: int = 1
    page_size: int = 20
    sort: str = "new"
    cid: Optional[int] = None

    #  天猫超市商品是否单件免邮，值为1：天猫超市商品单件免邮，
    #  此字段只针对天猫超市店铺商品有效，其它店铺商品无效
    tianmaochaoshi2: Optional[int] = None

    tianmaochaoshi: int = 1
