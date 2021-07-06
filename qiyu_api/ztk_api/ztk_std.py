"""
折淘客开放平台 标准化的 API
"""
import json
from datetime import datetime
from typing import Optional, List

import aiohttp
import structlog

from .bang_dan_tui_jian_args import BangDanTuiJianArgs
from .batch_item_args import BatchItemsArgs
from .batch_item_resp import BatchItemResp, BatchItemContentItem
from .gao_yong_args import GaoYongArgs
from .gao_yong_resp import GaoYongResp, GaoYongContentItem
from .guess_you_like_args import GuessYouLikeArgs
from .ju_hua_suan_args import JuHuaSuanArgs
from .keyword_args import KeywordArgs
from .nine_nine_args import NineNineArgs
from .search_args import SearchArgs
from .suggest_args import SuggestArgs
from .tmall_chao_shi_args import TMallChaoShiArgs
from .tmall_shang_pin_args import TMallShangPinArgs
from ..tbk_api import TbkItemInfo

__all__ = ["ZTKStd"]


def to_std_time(s: Optional[str]) -> Optional[datetime]:
    try:
        return datetime.fromisoformat(s)
    except ValueError:
        return None


class ZTKStd(object):
    """
    标准版本的 淘宝客 API
    折淘客 开放平台 API
    """

    def __init__(self, ztk_sid: str, logger: structlog.stdlib.BoundLogger):
        """
        :param logger: 日志记录器
        """
        self._http: Optional[aiohttp.ClientSession] = None
        self._sid = ztk_sid
        self._logger = logger

    async def gao_yong(self, args: GaoYongArgs) -> Optional[TbkItemInfo]:
        """
        高佣转链标准化
        """
        url = await args.to_http_url()
        ret = await self._do_query(url)
        resp = GaoYongResp(**ret)
        if resp.status != 200:
            self._logger.error(f"request ztk {url=} failed with: {resp=}")
            return None
        if len(resp.content) == 0:
            self._logger.info(f"ztk not find: tao_id={args.num_iid}")
            return None

        item_list: List[GaoYongContentItem] = list(
            map(lambda x: GaoYongContentItem(**x), resp.content)
        )

        item = self._find_best_coupon_link(item_list)

        coupon_recv_num = int(item.coupon_total_count) - int(item.coupon_remain_count)

        return TbkItemInfo(
            tao_id=item.tao_id,
            tao_img=item.pict_url,
            tao_link=item.item_url,
            tao_details=item.pcDescContent.split("|"),
            title_short=item.title,
            title_long=item.tao_title,
            price_origin=float(item.size),
            price_actual=float(item.quanhou_jiage),
            price_coupon=float(item.coupon_info_money),
            seller_id=item.seller_id,
            seller_name=item.shop_title,
            seller_logo=item.shopIcon,
            score_dsr=float(item.score1),
            score_ship=float(item.score3),
            score_service=float(item.score2),
            commission_rate=float(item.tkrate3),
            commission_money=float(item.tkfee3),
            sale_month=int(item.volume),
            sale_day=0,
            sale_two_hours=0,
            coupon_start_time=to_std_time(item.coupon_start_time),
            coupon_end_time=to_std_time(item.coupon_end_time),
            coupon_total_num=int(item.coupon_total_count),
            coupon_recv_num=coupon_recv_num,
            coupon_link=item.coupon_click_url,
            yun_fei_xian=item.yunfeixian == "1",
        )

    async def bang_dan_tui_jian(
        self, args: BangDanTuiJianArgs
    ) -> Optional[List[TbkItemInfo]]:
        """
        全天销量榜API：返回24小时内销量榜单商品列表（前600个），返回佣金≥15%，动态描述分≥4.6的商品列表。
        """
        url = await args.to_http_url()
        ret = await self._do_list_query_help(url)
        return ret

    async def batch_items(self, args: BatchItemsArgs) -> BatchItemResp:
        """
        批量获取 淘宝 信息

        :param args:
        :return:
        """
        url = await args.to_http_url()
        j = await self._do_query(url)
        return BatchItemResp(**j)

    async def guess_you_like(
        self, args: GuessYouLikeArgs
    ) -> Optional[List[TbkItemInfo]]:
        """
        猜你喜欢
        """
        url = await args.to_http_url()
        ret = await self._do_list_query_help(url)
        return ret

    async def ju_hua_suan(self, args: JuHuaSuanArgs) -> Optional[List[TbkItemInfo]]:
        """
        聚划算商品API：返回聚划算商品列表，返回佣金≥15%，动态描述分≥4.6的商品列表。
        """
        url = await args.to_http_url()
        ret = await self._do_list_query_help(url)
        return ret

    async def keyword(self) -> List[str]:
        """
        关键词词典API
        """
        args = KeywordArgs()
        url = await args.to_http_url()
        j = await self._do_query(url)
        if isinstance(j, dict):
            if j["status"] == 200:
                content = j["content"]
                assert isinstance(content, list)
                return list(map(lambda x: x["keywords"], content))
        return []

    async def nine_nine(self, args: NineNineArgs) -> Optional[List[TbkItemInfo]]:
        """
        9.9元商品API：返回购买价格≤9.9元的商品列表，返回佣金≥15%，动态描述分≥4.6的商品列表。
        """
        url = await args.to_http_url()
        ret = await self._do_list_query_help(url)
        return ret

    async def search(self, args: SearchArgs) -> Optional[List[TbkItemInfo]]:
        """
        全网搜索
        """
        url = await args.to_http_url()
        ret = await self._do_list_query_help(url)
        return ret

    async def suggest(self, args: SuggestArgs) -> Optional[List[str]]:
        """
        联想词
        """
        url = await args.to_http_url()
        j = await self._do_query(url)
        if not isinstance(j, dict):
            self._logger.warn("request ztk suggest failed")
            return None

        result = j["result"]

        return list(map(lambda item: item[0], result))

    async def tmall_chao_shi(
        self, args: TMallChaoShiArgs
    ) -> Optional[List[TbkItemInfo]]:
        """
        天猫超市商品API：返回天猫超市商品列表，动态描述分≥4.6的商品列表，根据不同参数可返回天猫超市单件免邮商品。
        """
        url = await args.to_http_url()
        ret = await self._do_list_query_help(url)
        return ret

    async def tmall_shang_pin(
        self, args: TMallShangPinArgs
    ) -> Optional[List[TbkItemInfo]]:
        """
        天猫商品API：返回天猫商品列表，返回佣金≥15%，动态描述分≥4.6的商品列表。
        """
        url = await args.to_http_url()
        ret = await self._do_list_query_help(url)
        return ret

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

    async def _do_list_query_help(self, url: str) -> Optional[List[TbkItemInfo]]:
        ret = await self._do_query(url)
        if ret.get("status", None) != 200:
            self._logger.error(f"ztk fetch {url=} failed: {ret=}")
            return None
        content = ret.get("content", [])
        if len(content) < 1:
            self._logger.warning(f"ztk fetch {url=} without data")
            return []
        tao_ids = list(map(lambda x: x["tao_id"], content))
        return await self._do_fetch_batch_items(tao_ids)

    async def _do_fetch_batch_items(
        self, tao_ids: List[str]
    ) -> Optional[List[TbkItemInfo]]:
        args = BatchItemsArgs(num_iids=",".join(tao_ids))
        ret = await self.batch_items(args)
        if ret.status != 200:
            self._logger.error(f"ztk fetch batch item {args=} failed: {ret=}")
            return None
        data_list = map(lambda x: BatchItemContentItem(**x), ret.content)

        def convert_item_to_std(item: BatchItemContentItem) -> TbkItemInfo:
            #
            # http://www.zhetaoke.com/user/extend/extend_lingquan_detail.aspx
            #
            coupon_recv_num = int(item.coupon_total_count) - int(
                item.coupon_remain_count
            )

            return TbkItemInfo(
                tao_id=item.tao_id,
                tao_img=item.pict_url,
                tao_link=item.item_url,
                tao_details=item.pcDescContent.split("|"),
                title_short=item.title,
                title_long=item.tao_title,
                price_origin=float(item.size),
                price_actual=float(item.quanhou_jiage),
                price_coupon=float(item.coupon_info_money),
                seller_id=item.seller_id,
                seller_name=item.shop_title,
                seller_logo=item.shopIcon,
                score_dsr=float(item.score1),
                score_ship=float(item.score3),
                score_service=float(item.score2),
                commission_rate=float(item.tkrate3),
                commission_money=float(item.tkfee3),
                sale_month=int(item.volume),
                sale_day=0,
                sale_two_hours=0,
                coupon_start_time=to_std_time(item.coupon_start_time),
                coupon_end_time=to_std_time(item.coupon_end_time),
                coupon_total_num=int(item.coupon_total_count),
                coupon_recv_num=coupon_recv_num,
                coupon_link=None,
                yun_fei_xian=item.yunfeixian == "1",
            )

        return list(map(convert_item_to_std, data_list))

    @staticmethod
    def _find_best_coupon_link(
        coupon_links: List[GaoYongContentItem],
    ) -> GaoYongContentItem:
        """
        从高佣返回列表中找到佣金最高的
        :param coupon_links:
        :return:
        """
        if len(coupon_links) == 1:
            return coupon_links[0]

        best = coupon_links[0]

        for item in coupon_links[1:]:
            # 当前 没有 coupon URL
            if best.coupon_click_url is None and item.coupon_click_url is not None:
                best = item
                continue

            # 当前 没有佣金 字段
            if best.tkfee3 is None and item.tkfee3 is not None:
                best = item
                continue

            # 当前 的佣金小于
            if best.tkfee3 is not None and item.tkfee3 is not None:
                if best.tkfee3 < item.tkfee3:
                    best = item
                    continue

        return best
