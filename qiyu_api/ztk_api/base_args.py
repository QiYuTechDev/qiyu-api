import os
from urllib import parse

from pydantic import BaseModel, Field


class BaseArgs(BaseModel):
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

    app_key: str = Field(
        None,
        title="折淘客的 app key",
        description="这个值通常不应该使用用户的传递值, 除非您构建自己的平台，允许用户使用自己的 app key",
    )

    @staticmethod
    def base_url() -> str:
        raise NotImplementedError

    def ztk_app_key(self) -> str:
        """
        获取 折淘客的 app key
        """
        if self.app_key is not None:
            return self.app_key

        app_key = os.getenv("ZTK_APP_KEY", None)
        if app_key is not None:
            return app_key

        raise NotImplementedError

    def to_http_query(self, appkey: str) -> str:
        """
        转换成 HTTP 的查询字符串
        :param appkey:
        :return:
        """
        d = self.dict(by_alias=True, exclude={"app_key"})
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
