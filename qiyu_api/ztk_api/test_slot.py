import os

import pytest
from structlog.stdlib import get_logger

from .gao_yong_args import GaoYongArgs
from .guess_you_like_args import GuessYouLikeArgs
from .search_args import SearchArgs
from .tkl_parse_args import TKLParseArgs
from .ztk_std import ZTKStd

sid = "49522"


def set_up_env():
    file = os.path.join(os.path.dirname(__file__), "../../dev.env")
    with open(file) as fp:
        lines = fp.readlines()
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        if line.startswith("#"):
            continue
        parts = line.split("=")
        if len(parts) != 2:
            continue
        k, v = parts
        os.environ.setdefault(k, v)


def get_ztk_std() -> ZTKStd:
    set_up_env()

    logger = get_logger()

    return ZTKStd(ztk_sid=sid, logger=logger)


def get_gao_yong_args(tao_id: str) -> GaoYongArgs:
    pid = "mm_1612410100_2210750041_111118250414"
    sid = "49522"
    return GaoYongArgs(pid=pid, num_iid=tao_id, sid=sid)


@pytest.mark.asyncio
async def test_guess_you_like_and_gao_yong():
    ztk = get_ztk_std()
    args = GuessYouLikeArgs()
    ret = await ztk.guess_you_like(args)
    assert ret is not None

    item = ret[0]
    args = get_gao_yong_args(item.tao_id)

    ret = await ztk.gao_yong(args)
    assert ret is not None
    print(ret)


@pytest.mark.asyncio
async def test_keyword():
    ztk = get_ztk_std()
    ret = await ztk.keyword()
    assert ret is not None
    print(ret)


@pytest.mark.asyncio
async def test_search_url():
    ztk = get_ztk_std()

    args = SearchArgs(
        q="https://detail.tmall.com/item.htm?id=627425639611&cm_id=140105335569ed55e27b"
    )

    data_list = await ztk.search(args)

    assert data_list is not None

    for item in data_list:
        args = get_gao_yong_args(item.tao_id)
        coupon_list = await ztk.gao_yong(args)
        print(coupon_list)


@pytest.mark.asyncio
async def test_tkl_parse():
    ztk = get_ztk_std()
    tkl = "1👈啊5NKkX84wYdk啊 https://m.tb.cn/h.4CEhFr0?sm=70d491 lofree洛斐 小浪无线机械键盘蓝牙双模电竞专用办公电脑茶轴84键"
    args = TKLParseArgs(content=tkl, sid=sid)
    tao_id = await ztk.tkl_parse(args=args)
    assert tao_id is not None
    args = get_gao_yong_args(tao_id)
    ret = await ztk.gao_yong(args)
    assert ret is not None
    print(ret)
