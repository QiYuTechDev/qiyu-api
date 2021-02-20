from dataclasses import dataclass
from typing import Optional

from .base_args import BaseArgs


@dataclass
class ItemDetailV2Args(BaseArgs):
    """
    全网商品详情API接口:

    返回全网商品详情信息，包含优惠券信息，可用来开发全网搜索等超级功能。

    :doc http://www.zhetaoke.com/user/extend/extend_lingquan_detail.aspx
    """

    @staticmethod
    def base_url():
        return "https://api.zhetaoke.com:10002/api/api_detail.ashx"

    tao_id: str
    code: Optional[str] = None
    num_iids: Optional[str] = None
    type: Optional[str] = None

    # the system will auto fill this value
    sid: Optional[str] = None
