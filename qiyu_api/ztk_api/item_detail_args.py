from dataclasses import dataclass
from typing import Optional

from .base_args import BaseArgs


@dataclass
class ItemDetailArgs(BaseArgs):
    """
    折淘客 全网商品详情接口参数

    :doc https://www.zhetaoke.com/user/open/open_item_info.aspx
    """

    @staticmethod
    def base_url():
        return "https://api.zhetaoke.com:10001/api/open_item_info.ashx"

    num_iids: str
    # the system will auto fill this value
    sid: Optional[str] = None
