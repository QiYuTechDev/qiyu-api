from dataclasses import dataclass
from typing import Optional

from .base_args import BaseArgs


@dataclass
class TKLCreateArgs(BaseArgs):
    """
    淘口令生成API：二合一链接、长链接、短链接等各种淘宝高佣链接，生成淘口令

    :doc https://www.zhetaoke.com/user/open/open_tkl_create.aspx
    """

    @staticmethod
    def base_url() -> str:
        return "https://api.zhetaoke.com:10001/api/open_tkl_create.ashx"

    # 口令跳转目标页，如：https://uland.taobao.com/，必须以https开头，
    # 可以是二合一链接、长链接、短链接等各种淘宝高佣链接；
    # 支持渠道备案链接。请注意，该参数需要进行Urlencode编码后传入。。
    #
    # 重要的事情说三遍：
    # 该参数需要进行Urlencode编码！
    # 该参数需要进行Urlencode编码！
    # 该参数需要进行Urlencode编码！
    url: str

    # taobao_appkey，自己淘客账号下，某个应用的appkey。
    taobao_appkey: str

    # taobao_appsecret，自己淘客账号下，某个应用的appsecret。
    taobao_appsecret: str

    # 口令弹框logoURL
    # 如：https://img.alicdn.com/bao/uploaded/i2.jpg_200x200.jpg
    logo: Optional[str] = None

    #  口令弹框内容，长度大于5个字符，如：美美小编精心推荐。
    #  尽量不要带特殊符号或特殊词，否则生成的淘口令手淘里可能打不开。
    text: str = "美美的小编精心推荐"

    #  值为1或者2，
    #  表示返回淘宝联盟请求地址，
    #  大家拿到地址后再用自己的服务器二次请求即可获得最终结果，
    #
    #  值为1返回http链接，
    #  值为2返回https安全链接，
    #  值为0表示直接返回淘口令最终结果。
    signurl: int = 0

    # 此字段只对signurl=0有效，signurl=1或2时，返回联盟请求地址。
    #
    # 生成淘口令结果类型，
    # type=0表示只返回淘口令，
    # type=1表示返回官方原始淘口令文案，支持IOS14版本。
    #
    # on iOS should use type = 1
    type: int = 0

    sid: str = ""
