from .api_sync import DtkSyncApi
from .gen import *
from .test_shared import get_app_key_and_secret, get_id, get_goods_id, get_uland_url

g_sync_api: Optional[DtkSyncApi] = None


def get_sync_api() -> DtkSyncApi:
    global g_sync_api
    if g_sync_api is None:
        key, secret = get_app_key_and_secret()
        g_sync_api = DtkSyncApi(key, secret)
    return g_sync_api


def test_super_category():
    dtk = get_sync_api()
    ret = dtk.category_get_super_category()
    assert ret is not None


def test_gen_category_get_super_category():
    dtk = get_sync_api()
    ret = dtk.category_get_super_category()
    assert ret is not None


def test_goods_price_trend():
    dtk = get_sync_api()
    args = GoodsPriceTrendArgs(id=get_id())
    ret = dtk.goods_price_trend(args)
    assert ret is not None


def test_goods_dtk_search():
    dtk = get_sync_api()
    args = GoodsGetDtkSearchGoodsArgs(keyWords="手机", pageId=str(1), pageSize=str(10))
    ret = dtk.goods_get_dtk_search_goods(args)
    assert ret is not None


def test_tb_service_get_privilege_link():
    dtk = get_sync_api()
    args = TbServiceGetPrivilegeLinkArgs(goodsId=get_goods_id())
    ret = dtk.tb_service_get_privilege_link(args)
    assert ret is not None


def test_goods_get_ranking_list():
    dtk = get_sync_api()
    args = GoodsGetRankingListArgs(rankType=str(1))
    ret = dtk.goods_get_ranking_list(args)
    assert ret is not None


def test_goods_get_goods_details():
    dtk = get_sync_api()
    args = GoodsGetGoodsDetailsArgs(id=get_id())
    ret = dtk.goods_get_goods_details(args)
    assert ret is not None


def test_tb_service_get_brand_list():
    dtk = get_sync_api()
    args = TbServiceGetBrandListArgs(pageId=str(1), pageSize=str(10))
    ret = dtk.tb_service_get_brand_list(args)
    assert ret is not None
    print(ret)


def test_goods_nine_op_goods_list():
    dtk = get_sync_api()
    args = GoodsNineOpGoodsListArgs(pageId=str(1), pageSize=str(10), nineCid=str(1))
    ret = dtk.goods_nine_op_goods_list(args)
    assert ret is not None


def test_tb_service_get_tb_service():
    dtk = get_sync_api()
    args = TbServiceGetTbServiceArgs(pageNo=str(1), pageSize=str(10), keyWords="苹果")
    ret = dtk.tb_service_get_tb_service(args)
    assert ret is not None


def test_category_get_top100():
    dtk = get_sync_api()
    ret = dtk.category_get_top100()
    assert ret is not None


def test_goods_get_goods_list():
    dtk = get_sync_api()
    args = GoodsGetGoodsListArgs(pageId=str(1), pageSize=str(10))
    ret = dtk.goods_get_goods_list(args)
    assert ret is not None


def test_goods_list_super_goods():
    dtk = get_sync_api()
    args = GoodsListSuperGoodsArgs(
        pageId=str(1), pageSize=str(10), keyWords="iOS", type=str(0)
    )
    ret = dtk.goods_list_super_goods(args)
    assert ret is not None


def test_goods_list_similer_goods_by_open():
    dtk = get_sync_api()
    args = GoodsListSimilerGoodsByOpenArgs(id=str(get_id()))
    ret = dtk.goods_list_similer_goods_by_open(args)
    assert ret is not None


def test_goods_search_suggestion():
    dtk = get_sync_api()
    args = GoodsSearchSuggestionArgs(keyWords="手机", type=str(1))
    ret = dtk.goods_search_suggestion(args)
    assert ret is not None


def test_goods_activity_catalogue():
    dtk = get_sync_api()
    ret = dtk.goods_activity_catalogue()
    assert ret is not None


def test_goods_activity_goods_list():
    dtk = get_sync_api()
    # todo impl dtk.goods_activity_goods_list()


def test_goods_topic_catalogue():
    dtk = get_sync_api()
    ret = dtk.goods_topic_catalogue()
    assert ret is not None


def test_goods_topic_goods_list():
    dtk = get_sync_api()
    # args = GoodsTopicGoodsListArgs()
    # ret = dtk.goods_topic_goods_list()


def test_category_ddq_goods_list():
    dtk = get_sync_api()
    args = CategoryDdqGoodsListArgs()
    ret = dtk.category_ddq_goods_list(args)
    assert ret is not None


def test_tb_service_parse_taokouling():
    dtk = get_sync_api()
    args = TbServiceParseTaokoulingArgs(content="1￥uFkCciFmKQH￥/")
    ret = dtk.tb_service_parse_taokouling(args)
    assert ret is not None


def test_tb_service_creat_taokouling():
    dtk = get_sync_api()
    args = TbServiceCreatTaokoulingArgs(text="hello", url=get_uland_url())
    ret = dtk.tb_service_creat_taokouling(args)
    assert ret is not None


def test_goods_exclusive_goods_list():
    dtk = get_sync_api()
    args = GoodsExclusiveGoodsListArgs(pageId=str(1), pageSize=str(10))
    ret = dtk.goods_exclusive_goods_list(args)
    assert ret is not None


def test_goods_explosive_goods_list():
    """guess you like API"""
    dtk = get_sync_api()
    args = GoodsExplosiveGoodsListArgs(pageId=str(1), pageSize=str(10))
    ret = dtk.goods_explosive_goods_list(args)
    assert ret is not None


def test_delanys_brand_get_goods_list():
    dtk = get_sync_api()
    args = DelanysBrandGetGoodsListArgs(
        brandId="30844", pageId=str(1), pageSize=str(10)
    )
    out = dtk.delanys_brand_get_goods_list(args)
    assert out is not None
    print(out)
