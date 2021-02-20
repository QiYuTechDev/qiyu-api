"""
折淘客 开放品台 API

"""
import json
from typing import Optional, List

import requests
import structlog

from .auth_account_args import AuthAccountArgs
from .bang_dan_tui_jian_args import BangDanTuiJianArgs
from .bang_dan_tui_jian_resp import BangDanTuiJianResp
from .channel_account_info_args import ChannelAccountInfoArgs
from .channel_id_list_args import ChannelIdListArgs
from .channel_invite_code_args import ChannelInviteCodeArgs
from .channel_save_record_args import ChannelSaveRecordArgs
from .gao_yong_args import GaoYongArgs
from .guess_you_like_args import GuessYouLikeArgs
from .guess_you_like_resp import GuessYouLikeResp
from .item_detail_args import ItemDetailArgs
from .item_detail_resp import ItemDetailResp
from .item_detail_v2_args import ItemDetailV2Args
from .item_detail_v2_resp import ItemDetailV2Resp
from .ju_hua_suan_args import JuHuaSuanArgs
from .ju_hua_suan_resp import JuHuaSuanResp
from .keyword_args import KeywordArgs
from .new_order_args import NewOrderArgs
from .nine_nine_args import NineNineArgs
from .nine_nine_resp import NineNineResp
from .search_args import SearchArgs
from .search_resp import SearchResp
from .suggest_args import SuggestArgs
from .tkl_create_args import TKLCreateArgs
from .tkl_create_resp import TKLCreateResp
from .tmall_chao_shi_args import TMallChaoShiArgs
from .tmall_chao_shi_resp import TmallChaoShiResp
from .tmall_shang_pin_args import TMallShangPinArgs
from .tmall_shang_pin_resp import TmallShangPinResp

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

    def bang_dan_tui_jian(self, args: BangDanTuiJianArgs) -> BangDanTuiJianResp:
        """
        全天销量榜API：返回24小时内销量榜单商品列表（前600个），返回佣金≥15%，动态描述分≥4.6的商品列表。
        """
        url = args.to_http_url_sync()
        j = self._do_query(url)
        return BangDanTuiJianResp.from_dict(j)

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

    def gao_yong(self, args: GaoYongArgs):
        """
        高佣转链API (商品ID)
        """
        args.sid = self._ztk_sid()

        url = args.to_http_url_sync()
        j = self._do_query(url)
        return j

    def guess_you_like(self, args: GuessYouLikeArgs) -> GuessYouLikeResp:
        """
        猜你喜欢
        """
        url = args.to_http_url_sync()
        j = self._do_query(url)
        return GuessYouLikeResp.from_dict(j)

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
        return ItemDetailV2Resp.from_dict(j)

    def ju_hua_suan(self, args: JuHuaSuanArgs) -> JuHuaSuanResp:
        """
        聚划算商品API：返回聚划算商品列表，返回佣金≥15%，动态描述分≥4.6的商品列表。
        """
        url = args.to_http_url_sync()
        j = self._do_query(url)
        return JuHuaSuanResp.from_dict(j)

    def keyword(self) -> list:
        """
        关键词词典API
        """
        args = KeywordArgs()
        url = args.to_http_url_sync()
        j = self._do_query(url)
        if isinstance(j, dict):
            if j["status"] == 200:
                content = j["content"]
                assert isinstance(content, list)
                return list(map(lambda x: x["keywords"], content))
        return []

    def new_order(self, args: NewOrderArgs) -> dict:
        """
        新订单获取
        """
        args.sid = self._ztk_sid()

        url = args.to_http_url_sync()
        j = self._do_query(url)
        return j

    def nine_nine(self, args: NineNineArgs):
        """
        9.9元商品API：返回购买价格≤9.9元的商品列表，返回佣金≥15%，动态描述分≥4.6的商品列表。
        """
        url = args.to_http_url_sync()
        j = self._do_query(url)
        return NineNineResp.from_dict(j)

    def search(self, args: SearchArgs) -> SearchResp:
        """
        全网搜索
        """
        url = args.to_http_url_sync()
        j = self._do_query(url)
        return SearchResp.from_dict(j)

    def suggest(self, args: SuggestArgs) -> Optional[List[str]]:
        """
        联想词
        """
        url = args.to_http_url_sync()
        j = self._do_query(url)
        if not isinstance(j, dict):
            self._logger.warn("request ztk suggest failed")
            return None

        result = j["result"]

        return list(map(lambda item: item[0], result))

    def tmall_chao_shi(self, args: TMallChaoShiArgs) -> TmallChaoShiResp:
        """
        天猫超市商品API：返回天猫超市商品列表，动态描述分≥4.6的商品列表，根据不同参数可返回天猫超市单件免邮商品。
        """
        url = args.to_http_url_sync()
        j = self._do_query(url)
        return TmallChaoShiResp.from_dict(j)

    def tmall_shang_pin(self, args: TMallShangPinArgs) -> TmallShangPinResp:
        """
        天猫商品API：返回天猫商品列表，返回佣金≥15%，动态描述分≥4.6的商品列表。
        """
        url = args.to_http_url_sync()
        j = self._do_query(url)
        return TmallShangPinResp.from_dict(j)

    def tkl_create(self, args: TKLCreateArgs) -> TKLCreateResp:
        """
        淘口令生成API：二合一链接、长链接、短链接等各种淘宝高佣链接，生成淘口令
        """
        args.sid = self._ztk_sid()

        url = args.to_http_url_sync()
        j = self._do_query(url)
        return TKLCreateResp.from_dict(j)

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
