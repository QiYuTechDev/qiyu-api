import os

import pytest

from .gen import *
from .test_shared import get_dtk_sync


def get_app_key_and_secret() -> (str, str):
    app_key = os.getenv("DTK_APP_KEY")
    app_secret = os.getenv("DTK_APP_SECRET")
    return app_key, app_secret


def test_simple():
    dtk = get_dtk_sync()
    args = GoodsNineOpGoodsListArgs(pageId=str(1), pageSize=str(10), nineCid=str(2))
    ret = dtk.goods_nine_op_goods_list(args=args)
    # print(json.dumps(ret, ensure_ascii=False))


def test_super_category():
    dtk = get_dtk_sync()
    ret = dtk.category_get_super_category()
    s = json.dumps(ret, ensure_ascii=False)
    # print(s)


@pytest.mark.asyncio
async def test_async_simple():
    app_key, app_secret = get_app_key_and_secret()
    args = GoodsNineOpGoodsListArgs(pageId=str(1), pageSize=str(10), nineCid=str(2))
    dtk = DtkAsync(app_key=app_key, app_secret=app_secret)
    ret = await dtk.goods_nine_op_goods_list(args=args)
    print(ret)
