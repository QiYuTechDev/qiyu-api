from .gen import *

from .test_shared import get_id, get_dtk_sync, get_goods_id


def test_gen_category_get_super_category():
    dtk = get_dtk_sync()
    ret = dtk.category_get_super_category()
    assert ret["code"] == 0
    print(ret)


def test_goods_price_trend():
    dtk = get_dtk_sync()
    args = GoodsPriceTrendArgs(id=get_id())
    ret = dtk.goods_price_trend(args)
    print(ret)
    assert ret["code"] == 0


def test_goods_get_dtk_search_goods():
    dtk = get_dtk_sync()
    args = GoodsGetDtkSearchGoodsArgs(keyWords="手机", pageId=str(1), pageSize=str(10))
    ret = dtk.goods_get_dtk_search_goods(args)
    print(ret)
    assert ret["code"] == 0


def test_tb_service_get_privilege_link():
    dtk = get_dtk_sync()
    args = TbServiceGetPrivilegeLinkArgs(goodsId=get_goods_id())
    ret = dtk.tb_service_get_privilege_link(args)
    print(ret)
    assert ret["code"] == 0


def test_goods_get_ranking_list():
    dtk = get_dtk_sync()
    args = GoodsGetRankingListArgs(rankType=str(1))
    ret = dtk.goods_get_ranking_list(args)
    assert ret["code"] == 0


def test_goods_get_goods_details():
    dtk = get_dtk_sync()
    args = GoodsGetGoodsDetailsArgs(id=get_id())
    ret = dtk.goods_get_goods_details(args)
    assert ret["code"] == 0


def test_tb_service_get_brand_list():
    dtk = get_dtk_sync()
    args = TbServiceGetBrandListArgs(pageId=str(1), pageSize=str(10))
    ret = dtk.tb_service_get_brand_list(args)
    assert ret["code"] == 0
    print(ret)


def test_goods_nine_op_goods_list():
    dtk = get_dtk_sync()
    args = GoodsNineOpGoodsListArgs(pageId=str(1), pageSize=str(10), nineCid=str(1))
    ret = dtk.goods_nine_op_goods_list(args)
    print(ret)
    assert ret["code"] == 0


def test_tb_service_get_tb_service():
    dtk = get_dtk_sync()
    args = TbServiceGetTbServiceArgs(pageNo=str(1), pageSize=str(10), keyWords="苹果")
    ret = dtk.tb_service_get_tb_service(args)
    print(ret)
    assert ret["code"] == 0


def test_category_get_top100():
    dtk = get_dtk_sync()
    ret = dtk.category_get_top100()
    print(ret)
    assert ret["code"] == 0


def test_category_ddq_goods_list():
    dtk = get_dtk_sync()
    args = CategoryDdqGoodsListArgs(roundTime="2020-12-18 15:00:00")
    ret = dtk.category_ddq_goods_list(args)
    print(ret)
