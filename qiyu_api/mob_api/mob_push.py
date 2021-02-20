from typing import Optional

from aiohttp import ClientSession

from .mob_push_base import MobPushBase

__all__ = ["MobPushApi"]


class MobPushApi(MobPushBase):
    """
    Mob Push SDK

    :doc: https://www.mob.com/wiki/detailed/?wiki=MobPushRestAPIfenlei1333&id=136
    """

    g_session: Optional[ClientSession] = None

    async def push_to_all(self, content: str):
        """
        推送给所有设备

        :doc: https://www.mob.com/wiki/detailed/?wiki=MobPushRestAPIfenlei1333&id=136

        :param content:  推送内容
        :return:
        """
        app_key = self._app_key

        data = {
            "source": "webapi",
            "appkey": app_key,
            "pushTarget": {
                "target": 1,  # 广播
            },
            "pushNotify": {
                "plats": [1],
                "content": content,
                "type": 1,
            },
        }

        await self._do_push(data, app_key)

    async def push(self, device: str, content: str):
        """
        推送一条消息

        :doc: https://www.mob.com/wiki/detailed/?wiki=MobPushRestAPIfenlei1333&id=136

        :return:
        """
        app_key = self._app_key

        data = {
            "source": "webapi",
            "appkey": app_key,
            "pushTarget": {
                "target": 4,
                "rids": [device],
            },
            "pushNotify": {
                "plats": [1],
                "content": content,
                "type": 1,
            },
        }

        await self._do_push(data, app_key)

    async def _do_push(self, data: dict, app_key: str):
        if self.g_session is None:
            self.g_session = ClientSession()

        sign = await self.sign_fun(data)
        headers = {"key": app_key, "sign": sign}

        async with self.g_session.post(
            self.s_push_url, data=data, headers=headers
        ) as ret:
            if 200 <= ret.status < 300:
                j = await ret.json()
                self._log.bind(data=data, ret=j).info("request mob push success")
            else:
                self._log.bind(data=data).error("request mob push failed")

    async def sign_fun(self, data: Optional[dict]) -> str:
        """
        计算 mob 的签名

        :param data:
        :return:
        """
        return self.compute_sign(data)
