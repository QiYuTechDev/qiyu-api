import os

import pytest
from structlog.stdlib import get_logger

from .gao_yong_args import GaoYongArgs
from .guess_you_like_args import GuessYouLikeArgs
from .ztk_std import ZTKStd


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


@pytest.mark.asyncio
async def test_guess_you_like_and_gao_yong():
    set_up_env()

    logger = get_logger()
    sid = "49522"

    ztk = ZTKStd(ztk_sid=sid, logger=logger)
    args = GuessYouLikeArgs()
    ret = await ztk.guess_you_like(args)
    assert ret is not None

    item = ret[0]
    tao_id = item.tao_id
    pid = "mm_1612410100_2210750041_111118250414"
    args = GaoYongArgs(pid=pid, num_iid=tao_id, sid=sid)

    ret = await ztk.gao_yong(args)
    assert ret is not None
    print(ret)


@pytest.mark.asyncio
async def test_keyword():
    set_up_env()

    logger = get_logger()
    sid = "49522"

    ztk = ZTKStd(ztk_sid=sid, logger=logger)
    ret = await ztk.keyword()
    assert ret is not None
    print(ret)
