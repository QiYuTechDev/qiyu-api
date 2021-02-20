from dataclasses import dataclass
from typing import Optional

from .base_args import BaseArgs


@dataclass
class NewOrderArgs(BaseArgs):
    """
    新订单获取

    https://www.zhetaoke.com/user/open/open_dingdanchaxun2.aspx
    """

    @staticmethod
    def base_url() -> str:
        return "https://api.zhetaoke.com:10001/api/open_dingdanchaxun2.ashx"

    start_time: str

    end_time: str

    # 查询时间类型
    # 1:按照订单淘客创建时间查询
    # 2:按照订单淘客付款时间查询
    # 3:按照订单淘客结算时间查询
    query_type: int

    # 位点，除第一页之外，都需要传递；
    # 前端原样返回。
    # 注意：
    # 从第二页开始，位点必须传递前一页返回的值，否则翻页无效。
    position_index: Optional[str] = None

    # 页大小，默认20，1~100
    page_size: int = 20

    # 推广者角色类型,
    # 2:二方，
    # 3:三方，
    # 不传，表示所有角色
    member_type: Optional[str] = None

    # 淘客订单状态，
    # 12-付款，
    # 13-关闭，
    # 14-确认收货（暂时无法结算佣金），
    # 3-结算成功;不传，表示所有状态
    tk_status: Optional[int] = None

    # 跳转类型，当向前或者向后翻页必须提供
    # -1: 向前翻页,
    # 1：向后翻页
    jump_type: Optional[int] = None

    # 第几页，默认1，1~100
    page_no: int = 1

    # 场景订单场景类型，
    # 1:常规订单，
    # 2:渠道订单，
    # 3:会员运营订单，
    # 默认为1
    order_scene: int = 2

    # 值为1或者2，表示返回淘宝联盟请求地址，
    # 大家拿到地址后再用自己的服务器二次请求即可获得最终结果，
    # 值为1返回http链接，
    # 值为2返回https安全链接。
    signurl: int = 2

    sid: str = ""
