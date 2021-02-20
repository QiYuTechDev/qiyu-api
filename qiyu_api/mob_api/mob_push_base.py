import hashlib
import json
from typing import Optional

from structlog.stdlib import BoundLogger

__all__ = ["MobPushBase"]


class MobPushBase(object):
    """
    Mob Push SDK (Base)

    :doc: https://www.mob.com/wiki/detailed/?wiki=MobPushRestAPIfenlei1333&id=136
    """

    s_push_url: str = "http://api.push.mob.com/v3/push/createPush"

    def __init__(self, logger: BoundLogger, app_key: str, app_secret: str):
        """
        :param logger:
        :param app_key: mob app key
        :param app_secret: mob app secret
        """
        self._log = logger
        self._app_key = app_key
        self._app_secret = app_secret

    def compute_sign(self, data: Optional[dict]) -> str:
        """
        计算 mob 的签名

        :param data: 要加密的数据
        :return:
        """
        if data is None:
            str_org = self._app_secret
        else:
            str_org = "%s%s" % (json.dumps(data), self._app_secret)

        return hashlib.md5(str_org.encode("utf-8")).hexdigest()
