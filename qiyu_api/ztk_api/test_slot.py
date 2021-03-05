import os

import pytest
from structlog.stdlib import get_logger

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
async def test_guess_you_like():
    set_up_env()

    logger = get_logger()
    ztk = ZTKStd(ztk_sid="49522", logger=logger)
    args = GuessYouLikeArgs()
    ret = await ztk.guess_you_like(args)
    assert ret is not None
    print(ret)
