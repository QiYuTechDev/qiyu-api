"""
测试共享模块
"""
import os

from .gen import *


def get_app_key_and_secret() -> (str, str):
    app_key = os.getenv("DTK_APP_KEY")
    app_secret = os.getenv("DTK_APP_SECRET")
    if app_key is None or app_secret is None:
        with open(os.path.join(os.path.dirname(__file__), "..", "secret.json")) as fp:
            d = json.load(fp)
            app_key = d["app_key"]
            app_secret = d["app_secret"]
    return app_key, app_secret


def get_dtk_sync() -> DtkSync:
    app_key, app_secret = get_app_key_and_secret()
    return DtkSync(app_key=app_key, app_secret=app_secret)


def get_id() -> str:
    dtk = get_dtk_sync()
    args = GoodsGetDtkSearchGoodsArgs(keyWords="手机", pageId=str(1), pageSize=str(10))
    ret = dtk.goods_get_dtk_search_goods(args)
    assert ret["code"] == 0
    return ret["data"]["list"][0]["id"]


def get_uland_url() -> str:
    dtk = get_dtk_sync()
    goods_id = get_goods_id()
    args = GoodsGetGoodsDetailsArgs(id="", goodsId=goods_id)
    ret = dtk.goods_get_goods_details(args)
    return ret["data"]["couponLink"]


def get_goods_id() -> str:
    dtk = get_dtk_sync()
    args = GoodsGetDtkSearchGoodsArgs(keyWords="手机", pageId=str(1), pageSize=str(10))
    ret = dtk.goods_get_dtk_search_goods(args)
    assert ret["code"] == 0
    return ret["data"]["list"][0]["goodsId"]
