import os
from urllib import parse

from dataclasses_json import DataClassJsonMixin


class BaseArgs(DataClassJsonMixin):
    """
    折淘客基础请求数据类型

    子类的字段值为: None 的 key 会被过滤掉
    例如:
    f1: Optional[str] = None

    注意:
    字段值为 '' (空字符串) 的不会被过滤掉
    例如:
    f2: str = ''
    在个参数中会变成:
    'f2='
    """

    @staticmethod
    def base_url() -> str:
        raise NotImplemented

    @staticmethod
    def ztk_app_key() -> str:
        """
        获取 折淘客的 app key
        """
        app_key = os.getenv("ZTK_APP_KEY", None)
        if app_key is not None:
            return app_key
        raise NotImplemented

    def to_http_query(self, appkey: str) -> str:
        """
        转换成 HTTP 的查询字符串
        :param appkey:
        :return:
        """
        d = self.to_dict()
        dks = []
        for k in d.keys():
            if d[k] is None:
                dks.append(k)

        for dk in dks:
            d.pop(dk)

        d["appkey"] = appkey
        return parse.urlencode(d)

    async def to_http_url(self) -> str:
        """
        转换成 HTTP 的请求 URL
        :return:
        """
        app_key = self.ztk_app_key()
        query = self.to_http_query(app_key)
        url = self.base_url()
        return f"{url}?{query}"

    def to_http_url_sync(self) -> str:
        """
        同步版本的 转换成 HTTP 请求
        :return:
        """
        app_key = self.ztk_app_key()
        query = self.to_http_query(app_key)
        url = self.base_url()
        return f"{url}?{query}"
