from dataclasses import dataclass
from typing import Optional

from .base_args import BaseArgs


@dataclass
class ChannelInviteCodeArgs(BaseArgs):
    """
    淘宝客邀请码生成API：生成邀请码，然后让用户进行渠道备案，生成新的渠道ID

    :doc https://www.zhetaoke.com/user/open/open_sc_invitecode_get.aspx
    """

    @staticmethod
    def base_url() -> str:
        return "https://api.zhetaoke.com:10001/api/open_sc_invitecode_get.ashx"

    # 渠道推广的物料类型，示例值：common
    relation_app: str

    #  邀请码类型
    #  1 - 渠道邀请，
    #  2 - 渠道裂变，
    #  3 - 会员邀请
    code_type: int

    #  渠道关系ID
    relation_id: Optional[str] = None

    sid: Optional[str] = None
