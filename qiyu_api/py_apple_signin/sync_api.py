from typing import Union, Optional

from requests import Session

from .dt import AppleConfig, AppleSignInSuccessRet, AppleSignInFailureRet
from .shared import Shared

__all__ = ["AppleSignInApi"]


class AppleSignInApi(Shared):
    """
    苹果登陆同步处理接口
    """

    def __init__(self, config: AppleConfig):
        super().__init__(config)
        self._session = Session()

    def try_auth(
        self, code: str
    ) -> Optional[Union[AppleSignInSuccessRet, AppleSignInFailureRet]]:
        """
        尝试进行 code 的认证
        :param code: 授权code
        :return:
        """
        headers, data = self._make_up_data(code)

        token_url = self.ACCESS_TOKEN_URL

        resp = self._session.post(token_url, data=data, headers=headers)
        if not resp.ok:
            # network or apple server is down
            return None

        ret = resp.json()
        assert isinstance(ret, dict)
        if "error" in ret:
            return AppleSignInFailureRet.from_dict(ret)
        else:
            return AppleSignInSuccessRet.from_dict(ret)
