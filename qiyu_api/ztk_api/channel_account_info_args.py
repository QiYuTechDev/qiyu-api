from dataclasses import dataclass

from .base_args import BaseArgs


@dataclass
class ChannelAccountInfoArgs(BaseArgs):
    """
    淘宝客渠道信息查询API：获取渠道ID信息列表

    :doc https://www.zhetaoke.com/user/open/open_sc_publisher_get.aspx
    """

    @staticmethod
    def base_url() -> str:
        return "https://api.zhetaoke.com:10001/api/open_sc_publisher_get.ashx"

    #  渠道推广的物料类型，示例值：common
    relation_app: str

    #  渠道备案 - 渠道关系ID
    relation_id: int

    # 第几页
    page_no: int

    # 每页大小
    page_size: int

    #  类型，必选 默认为1
    info_type: int = 1

    sid: str = ""
