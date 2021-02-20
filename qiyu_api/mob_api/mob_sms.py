import base64
import hashlib
import json
import time
from typing import Optional

import requests
from pyDes import *  # noqa
from structlog.stdlib import BoundLogger

__all__ = ["MobSmsApi"]


class MobSmsApi(object):
    """
    掌淘科技 SMS 认证 API 接口
    """

    def __init__(self, logger: BoundLogger, app_key: str, app_secret: str):
        self._log = logger
        self._app_key = app_key
        self._app_secret = app_secret

    def sms_verify(
        self, mob_token: str, op_token: str, operator: str, md5: str
    ) -> Optional[str]:
        """
        sms token 认证

        :param mob_token:
        :param op_token:
        :param operator:
        :param md5: android md5 验证码
        :return: 成功返回手机号 失败返回 None
        """
        url = "http://identify.verify.mob.com/auth/auth/sdkClientFreeLogin"
        app_key = self._app_key

        data = {
            "appkey": app_key,
            "token": mob_token,
            "opToken": op_token,
            "operator": operator,
            "timestamp": int(time.time() * 1000),
            "md5": md5,
        }

        data["sign"] = self._generate_sign(data, self._app_secret)

        ret = requests.post(url, json=data)
        if not ret.ok:
            self._log.bind(ret=ret).error("request mob tech failed")
            return None

        ret = ret.json()

        if ret["status"] != 200:
            self._log.bind(data=ret).error("invalid status")
            return None

        k = des(  # noqa
            self._app_secret[:8], CBC, "00000000", pad=None, padmode=PAD_PKCS5  # noqa
        )
        b: bytes = k.decrypt(base64.b64decode(ret["res"]))
        # b'{"isValid":1,"phone":"18600825785","valid":true}'
        t = b.decode()
        d = json.loads(t)
        if d["isValid"] == 1:
            self._log.bind(data=d).info("mob ret success")
            return d["phone"]
        else:
            self._log.bind(data=d).error("mob tech check invalid")
            return None

    @staticmethod
    def _generate_sign(request: dict, secret: str) -> str:
        ret = ""
        stmp = sorted(request.items(), key=lambda d: d[0])
        for i in stmp:
            ret += i[0] + "=" + str(i[1]) + "&"
        return hashlib.md5((ret[:-1] + secret).encode("utf-8")).hexdigest()
