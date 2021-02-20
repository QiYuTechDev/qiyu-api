from dataclasses import dataclass
from typing import Optional

from .base_args import BaseArgs


@dataclass
class ChannelSaveRecordArgs(BaseArgs):
    """
    淘宝客渠道备案API：用户进行渠道备案，生成新的渠道ID。
    支持渠道备案和会员备案

    :doc https://www.zhetaoke.com/user/open/open_sc_publisher_save.aspx
    """

    @staticmethod
    def base_url() -> str:
        return "https://api.zhetaoke.com:10001/api/open_sc_publisher_save.ashx"

    # 淘宝客邀请渠道的邀请码
    inviter_code: str

    #  代理授权，并登记备案后，返回渠道信息至回调地址
    backurl: str

    # 淘宝客邀请会员的邀请码
    inviter_code_s: Optional[str] = None

    #  淘客授权页面类型
    #  1：电脑版授权页面
    #  0：手机版授权页面
    #  默认值1
    type: Optional[int] = None

    #  渠道备注，此内容建议填写用户唯一标识（比如用户编号，账号等唯一字段），
    #  跟返回的relation_id字段做关联。
    s_note: Optional[str] = None
