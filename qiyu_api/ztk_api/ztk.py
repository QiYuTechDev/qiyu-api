import json
from typing import Optional

import aiohttp
import structlog

from .auth_account_args import AuthAccountArgs
from .batch_item_args import BatchItemsArgs
from .batch_item_resp import BatchItemResp
from .channel_account_info_args import ChannelAccountInfoArgs
from .channel_id_list_args import ChannelIdListArgs
from .channel_invite_code_args import ChannelInviteCodeArgs
from .channel_save_record_args import ChannelSaveRecordArgs
from .item_detail_resp import ItemDetailResp
from .item_detail_v2_args import ItemDetailV2Args
from .item_detail_v2_resp import ItemDetailV2Resp
from .new_order_args import NewOrderArgs
from .tkl_create_args import TKLCreateArgs
from .tkl_create_resp import TKLCreateResp

__all__ = ["ZTK"]


class ZTK(object):
    """
    折淘客 开放平台 API
    """

    def __init__(self, ztk_sid: str, logger: structlog.stdlib.BoundLogger):
        """
        :param logger: 日志记录器
        """
        self._http: Optional[aiohttp.ClientSession] = None
        self._sid = ztk_sid
        self._logger = logger

    async def auth_account(self, args: AuthAccountArgs):
        """
        获取账户授权列表API接口
        """
        args.sid = await self._ztk_sid()

        url = await args.to_http_url()
        j = await self._do_query(url)
        return j

    async def batch_items(self, args: BatchItemsArgs) -> BatchItemResp:
        """
        批量获取 淘宝 信息

        :param args:
        :return:
        """
        url = await args.to_http_url()
        j = await self._do_query(url)
        return BatchItemResp(**j)

    async def channel_account_info(self, args: ChannelAccountInfoArgs):
        args.sid = await self._ztk_sid()

        url = await args.to_http_url()
        j = await self._do_query(url)
        return j

    async def channel_id_list(self, args: ChannelIdListArgs):
        args.sid = await self._ztk_sid()
        url = await args.to_http_url()
        j = await self._do_query(url)
        return j

    async def channel_invite_code(self, args: ChannelInviteCodeArgs):
        """
        淘宝客邀请码生成API：生成邀请码，然后让用户进行渠道备案，生成新的渠道ID
        """
        args.sid = await self._ztk_sid()

        url = await args.to_http_url()
        j = await self._do_query(url)
        return j

    async def channel_save_record(self, args: ChannelSaveRecordArgs):
        """
        淘宝客渠道备案API：用户进行渠道备案，生成新的渠道ID。
        """
        url = await args.to_http_url()
        j = await self._do_query(url)
        return j

    async def item_detail_v2(self, args: ItemDetailV2Args) -> ItemDetailV2Resp:
        args.sid = await self._ztk_sid()

        url = await args.to_http_url()
        j = await self._do_query(url)
        return ItemDetailV2Resp(**j)

    async def new_order(self, args: NewOrderArgs):
        """
        新订单获取
        """
        args.sid = await self._ztk_sid()

        url = await args.to_http_url()
        j = await self._do_query(url)
        return ItemDetailResp.from_ztk_resp(j)

    async def tkl_create(self, args: TKLCreateArgs) -> TKLCreateResp:
        """
        淘口令生成API：二合一链接、长链接、短链接等各种淘宝高佣链接，生成淘口令
        """
        args.sid = await self._ztk_sid()

        url = await args.to_http_url()
        j = await self._do_query(url)
        return TKLCreateResp(**j)

    async def do_query(self, url: str) -> dict:
        """
        这是给外部使用的函数

        :param url:
        :return:
        """
        return await self._do_query(url)

    async def _do_query(self, url: str) -> dict:
        if self._http is None:
            self._http = aiohttp.ClientSession()

        async with self._http.get(url) as result:
            text = await result.text()
            return json.loads(text)

    async def _ztk_sid(self) -> Optional[str]:
        """
        获取 折淘客的 sid
        """
        return self._sid
