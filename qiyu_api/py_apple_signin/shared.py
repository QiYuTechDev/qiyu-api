from datetime import datetime, timedelta
from typing import Tuple

import jwt

from .dt import AppleConfig

__all__ = ["Shared"]


class Shared(object):
    """
    shared code between sync and async version
    """

    ACCESS_TOKEN_URL = "https://appleid.apple.com/auth/token"

    def __init__(self, config: AppleConfig):
        """
        :param config: 配置项目
        """
        self._config = config

    def _make_up_data(self, code: str) -> Tuple[dict, dict]:
        """
        组装需要发送的数据

        :param code: Apple SignIn 在客户端获取到的 授权码 (aka: authorizationCode)
        :return: (headers, data)
        """
        client_id = self._config.bundle_id
        client_secret = self._client_secret()

        headers = {"content-type": "application/x-www-form-urlencoded"}
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "grant_type": "authorization_code",
        }

        return headers, data

    def _client_secret(self) -> str:
        headers = {"key_id": self._config.key_id}

        payload = {
            "iss": self._config.team_id,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(days=180),
            "aud": "https://appleid.apple.com",
            "sub": self._config.bundle_id,
        }

        private_key = self._config.private_key

        return jwt.encode(
            payload, private_key, algorithm="ES256", headers=headers
        ).decode("utf-8")
