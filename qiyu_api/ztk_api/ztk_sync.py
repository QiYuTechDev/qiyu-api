"""
折淘客 开放品台 API

"""
import json
from typing import Optional

import requests
import structlog

from .auth_account_args import AuthAccountArgs
from .channel_account_info_args import ChannelAccountInfoArgs
from .channel_id_list_args import ChannelIdListArgs
from .channel_invite_code_args import ChannelInviteCodeArgs
from .channel_save_record_args import ChannelSaveRecordArgs
from .item_detail_args import ItemDetailArgs
from .item_detail_resp import ItemDetailResp
from .item_detail_v2_args import ItemDetailV2Args
from .item_detail_v2_resp import ItemDetailV2Resp
from .new_order_args import NewOrderArgs
from .tkl_create_args import TKLCreateArgs
from .tkl_create_resp import TKLCreateResp

__all__ = ["ZTKSync"]


class ZTKSync(object):
    """
    折淘客 开放平台 API
    """

    def __init__(self, ztk_sid: str, logger: structlog.stdlib.BoundLogger):
        """
        :param logger: 日志记录器
        """
        self._http: requests.Session = requests.session()
        self._sid = ztk_sid
        self._logger = logger

    def auth_account(self, args: AuthAccountArgs):
        """
        获取账户授权列表API接口
        """
        args.sid = self._ztk_sid()

        url = args.to_http_url_sync()
        j = self._do_query(url)
        return j

    def channel_account_info(self, args: ChannelAccountInfoArgs):
        args.sid = self._ztk_sid()

        url = args.to_http_url_sync()
        j = self._do_query(url)
        return j

    def channel_id_list(self, args: ChannelIdListArgs):
        args.sid = self._ztk_sid()

        url = args.to_http_url_sync()
        j = self._do_query(url)
        return j

    def channel_invite_code(self, args: ChannelInviteCodeArgs):
        """
        淘宝客邀请码生成API：生成邀请码，然后让用户进行渠道备案，生成新的渠道ID
        """
        args.sid = self._ztk_sid()

        url = args.to_http_url_sync()
        j = self._do_query(url)
        return j

    def channel_save_record(self, args: ChannelSaveRecordArgs):
        """
        淘宝客渠道备案API：用户进行渠道备案，生成新的渠道ID。
        """
        url = args.to_http_url_sync()
        j = self._do_query(url)
        return j

    def item_detail(self, args: ItemDetailArgs) -> ItemDetailResp:
        """
        折淘客 全网商品详情接口参数
        """
        args.sid = self._ztk_sid()

        url = args.to_http_url_sync()
        j = self._do_query(url)
        try:
            return ItemDetailResp.from_ztk_resp(j)
        except Exception as e:
            self._logger.bind(exec=e).error("item detail error")
            raise

    def item_detail_v2(self, args: ItemDetailV2Args) -> ItemDetailV2Resp:
        args.sid = self._ztk_sid()

        url = args.to_http_url_sync()
        j = self._do_query(url)
        return ItemDetailV2Resp(**j)

    def new_order(self, args: NewOrderArgs) -> dict:
        """
        新订单获取
        """
        args.sid = self._ztk_sid()

        url = args.to_http_url_sync()
        j = self._do_query(url)
        return j

    def tkl_create(self, args: TKLCreateArgs) -> TKLCreateResp:
        """
        淘口令生成API：二合一链接、长链接、短链接等各种淘宝高佣链接，生成淘口令
        """
        args.sid = self._ztk_sid()

        url = args.to_http_url_sync()
        j = self._do_query(url)
        return TKLCreateResp(**j)

    def do_query(self, url: str) -> dict:
        """
        这是给外部使用的函数

        :param url:
        :return:
        """
        return self._do_query(url)

    def _do_query(self, url: str) -> dict:
        self._http.get(url)
        ret = self._http.get(url)
        if ret.ok:
            return json.loads(ret.text)

    def _ztk_sid(self) -> Optional:
        return self._sid
