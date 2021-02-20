from dataclasses import dataclass

from .base_args import BaseArgs


@dataclass
class BatchItemsArgs(BaseArgs):
    """
    批量全网商品详情API接口：可同时获取20个商品的全网商品详情信息
    包含优惠券信息，可用来批量获取商品详情信息等超级功能。

    :doc http://www.zhetaoke.com/user/extend/extend_lingquan_detail_piliang.aspx
    """

    @staticmethod
    def base_url() -> str:
        return "https://api.zhetaoke.com:10002/api/api_detail_piliang.ashx"

    num_iids: str
    """
    多个商品ID串，用英文逗号,分割，最大20个。
    该接口可以用来批量获取商品详情信息，包含优惠券信息、佣金信息等。
    该接口支持全网所有淘宝客商品。
    """

    def set_item_ids(self, ids: [str]):
        self.num_iids = ",".join(ids)
