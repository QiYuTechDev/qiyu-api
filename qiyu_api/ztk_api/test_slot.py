import pytest
from structlog.stdlib import get_logger

from .guess_you_like_args import GuessYouLikeArgs
from .ztk_std import ZTKStd


@pytest.mark.asyncio
async def test_guess_you_like():
    logger = get_logger()
    ztk = ZTKStd(ztk_sid="49522", logger=logger)
    args = GuessYouLikeArgs()
    ret = await ztk.guess_you_like(args)
    assert ret is not None
    print(ret)
