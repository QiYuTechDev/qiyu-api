from dataclasses import dataclass
from typing import Optional

from .base_args import BaseArgs


@dataclass
class GuessYouLikeArgs(BaseArgs):
    """
    折淘客 猜你喜欢接口参数

    :doc https://www.zhetaoke.com/user/open/open_item_guess_like.aspx
    """

    @staticmethod
    def base_url():
        return "https://api.zhetaoke.com:10001/api/open_item_guess_like.ashx"

    page: int = 1
    """
    分页获取数据,第几页
    """

    page_size: int = 20
    """
    每页数据条数（默认每页20条），可自定义1-50之间
    """

    sort: str = "new"
    """
    商品排序方式，
    new：按照综合排序，
    total_sale_num_asc：按照总销量从小到大排序，total_sale_num_desc：按照总销量从大到小排序，
    sale_num_asc：按照月销量从小到大排序，sale_num_desc：按照月销量从大到小排序，
    commission_rate_asc：按照佣金比例从小到大排序，commission_rate_desc：按照佣金比例从大到小排序，
    price_asc：按照价格从小到大排序，price_desc：按照价格从大到小排序，
    coupon_info_money_asc：按照优惠券金额从小到大排序，coupon_info_money_desc：按照优惠券金额从大到小排序，
    shop_level_asc：按照店铺等级从低到高排序，shop_level_desc：按照店铺等级从高到低排序，
    tkfee_asc：按照返佣金额从低到高排序，tkfee_desc：按照返佣金额从高到低排序，
    code：按照code值从大到小排序，date_time：按照更新时间排序，random：按照随机排序
    """

    device_value: Optional[str] = None
    """
    设备号加密后的值（MD5加密需32位小写）
    """

    device_encrypt: Optional[str] = None
    """
    设备号加密类型：MD5
    """

    device_type: Optional[str] = None
    """
    设备号类型：IMEI，或者IDFA，或者UTDID（UTDID不支持MD5加密）
    """

    item_id: Optional[str] = None
    """
    商品ID：如果该值非空，那么device_value、device_encrypt和device_type无效，反之，如果这三个值非空，那么商品ID无效
    """
