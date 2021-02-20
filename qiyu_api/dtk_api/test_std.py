import pytest

from .api_async import DtkAsyncApi
from .api_std import DtkStdApi
from .gen import GoodsNineOpGoodsListArgs, GoodsListSuperGoodsArgs
from .test_shared import get_app_key_and_secret


@pytest.mark.asyncio
async def test_multi():
    app_key, secret = get_app_key_and_secret()

    args = GoodsNineOpGoodsListArgs(pageId=str(1), pageSize="20", nineCid="1")
    dtk = DtkAsyncApi(app_key=app_key, app_secret=secret)
    ret = await dtk.goods_nine_op_goods_list(args)
    tao_ids = []
    for item in ret.list:
        tao_ids.append(item.goodsId)

    std = DtkStdApi(app_key=app_key, app_secret=secret)
    ret = await std.get_multi_goods_detail(tao_ids)
    print(ret)


@pytest.mark.asyncio
async def test_super_search():
    app_key, secret = get_app_key_and_secret()

    a1 = GoodsListSuperGoodsArgs(pageId="1", pageSize="20", keyWords="裤子", type="0")
    a2 = GoodsListSuperGoodsArgs(
        pageId="1", pageSize="20", keyWords="裤子", type="0", sort="total_sales_asc"
    )
    a3 = GoodsListSuperGoodsArgs(
        pageId="1", pageSize="20", keyWords="裤子", type="0", sort="price_asc"
    )

    dtk = DtkStdApi(app_key=app_key, app_secret=secret)
    for args in [a1, a2]:
        j = await dtk.goods_list_super_goods(args)
        assert j is not None
