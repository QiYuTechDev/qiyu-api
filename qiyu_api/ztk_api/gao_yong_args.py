from dataclasses import dataclass
from typing import Optional

from .base_args import BaseArgs


@dataclass
class GaoYongArgs(BaseArgs):
    """
    高佣转链API (商品ID)

    :doc: https://www.zhetaoke.com/user/open/open_gaoyongzhuanlian.aspx
    """

    @staticmethod
    def base_url() -> str:
        return "https://api.zhetaoke.com:10001/api/open_gaoyongzhuanlian.ashx"

    # 淘客PID，mm_xxx_xxx_xxx,三段格式，必须与授权的账户相同，否则出错
    pid: str

    # 商品ID,商品ID或me必须填一个
    num_iid: Optional[str] = None

    # 团长与下游渠道合作的特殊标识，用于统计渠道推广效果
    xid: Optional[str] = None

    # 渠道关系ID，仅适用于渠道推广场景。
    relation_id: Optional[str] = None

    # 会员运营ID
    special_id: Optional[str] = None

    # 淘宝客外部用户标记，如自身系统账户ID；微信ID等
    external_id: Optional[str] = None

    # signurl=5，返回结果整合高佣转链API、解析商品编号API、全网商品详情API、淘口令创建API，已经自动判断和拼接使用全网G券还是全网S券。
    # signurl=4，返回结果整合高佣转链API、解析商品编号API、商品简版详情API、淘口令创建API，已经自动判断和拼接使用全网G券还是全网S券。
    # signurl=3，返回结果整合高佣转链API、解析商品编号API，已经自动判断和拼接使用全网G券还是全网S券。
    # signurl=0或1或2，返回官方高佣转链接口结果，需要自行判断和拼接使用全网G券或者全网S券。
    # signurl=0，表示直接返回最终结果。
    # signurl=1或2，表示返回淘宝联盟请求地址，大家拿到地址后再用自己的服务器二次请求即可获得最终结果，值为1返回http链接，值为2返回https安全链接。
    signurl: int = 5

    # 对应的淘客账号授权ID点击查看
    sid: str = ""
