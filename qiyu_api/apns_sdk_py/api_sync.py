from requests import Session, Response

from .dt import *

__all__ = ['APNsSync']


class APNsSync(object):

    def __init__(self, base_url: str):
        self._base_url = base_url
        self._session = Session()

    def push(self, form: PushForm) -> bool:
        """
        推送一条信息给 iOS 设备

        推送消息给 指定的 iOS 设备
        """
        url = self._get_url_by_path("/push")
        resp = self._do_request(method="POST", url=url, data=form.to_dict())

        if resp.ok:
            return True
        else:
            return False

    def _get_url_by_path(self, path: str) -> str:
        return f'{self._base_url}{path}'

    def _do_request(self, method: str, url: str, data: dict) -> Response:
        return self._session.request(method=method, url=url, json=data)
