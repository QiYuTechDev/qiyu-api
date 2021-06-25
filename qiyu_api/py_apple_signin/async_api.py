from typing import Union, Optional

from aiohttp.client import ClientSession

from .dt import AppleConfig
from .dt import AppleSignInSuccessRet, AppleSignInFailureRet
from .shared import Shared

__all__ = ["AppleSignInAsyncApi"]


class AppleSignInAsyncApi(Shared):
    """
    苹果登陆异步处理接口

    Apple SignIn async process interface
    """

    def __init__(self, config: AppleConfig):
        super().__init__(config)
        self._session = ClientSession()

    async def try_auth(
        self, code: str
    ) -> Optional[Union[AppleSignInSuccessRet, AppleSignInFailureRet]]:
        """
        尝试进行 code 的认证
        :param code: 授权code
        :return:
        """
        headers, data = self._make_up_data(code)

        resp = await self._session.post(
            self.ACCESS_TOKEN_URL, data=data, headers=headers
        )
        if not (200 <= resp.status < 300):
            # network or apple server is down
            return None

        ret = await resp.json()
        assert isinstance(ret, dict)
        if "error" in ret:
            return AppleSignInFailureRet(**ret)
        else:
            return AppleSignInSuccessRet(**ret)
