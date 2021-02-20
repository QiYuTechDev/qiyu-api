from dataclasses import dataclass
from typing import Optional

from .base_args import BaseArgs


@dataclass
class ChannelIdListArgs(BaseArgs):
    @staticmethod
    def base_url():
        return "https://api.zhetaoke.com:10001/api/open_sc_publisher_get.ashx"

    info_type: int
    """
    类型，必选 1:渠道信息；2:会员信息
    """

    relation_id: Optional[int] = None
    """
    渠道备案 - 渠道关系ID
    """

    special_id: Optional[int] = None
    """
    会员运营ID
    """

    external_id: Optional[str] = None
    """
    淘宝客外部用户标记，如自身系统账户ID；微信ID等
    """

    page_no: int = 1
    """
    第几页
    """

    page_size: int = 20
    """
    每页大小
    """

    relation_app: str = "common"
    """
    渠道推广的物料类型，示例值：common
    """

    sid: str = ""
    """
    对应的淘客账号授权ID
    """
