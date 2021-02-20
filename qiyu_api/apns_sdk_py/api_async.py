from aiohttp.client import ClientResponse

from .dt import *

__all__ = ['APNsAsync']


class APNsAsync(object):
    def __init__(self, base_url: str):
        self._base_url = base_url
        self._session = None

    async def push(self, form: PushForm) -> bool:
        """
        推送一条信息给 iOS 设备

        推送消息给 指定的 iOS 设备
        """
        url = self._get_url_by_path("/push")
        resp = await self._do_request(method="POST", url=url, data=form.to_dict())

        if 200 <= resp.status < 300:
            return True
        else:
            return False

    def _get_url_by_path(self, path: str) -> str:
        return f'{self._base_url}{path}'

    async def _do_request(self, method: str, url: str, data: dict) -> ClientResponse:
        return await self._session.request(method=method, url=url, json=data)
