from typing import Optional

from .base_args import BaseArgs


class AuthAccountArgs(BaseArgs):
    """
    获取账户授权列表API接口

    :doc https://www.zhetaoke.com/user/open/open_taokeshouquaninfo.aspx
    """

    @staticmethod
    def base_url() -> str:
        return " 接口地址：https://api.zhetaoke.com:10001/api/open_taokeshouquaninfo.ashx "

    #  第几页，每页最多返回100个
    page: Optional[int] = None

    #  还剩下几天授权过期，取值范围0-7之间的整数，
    #  比如值为3，表示获取还剩下3天授权过期淘客账号信息
    expire_day: Optional[int] = None

    # 对应的淘客账号授权ID
    sid: str = ""
