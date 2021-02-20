import base64
import hmac
import secrets
import time
from datetime import datetime
from urllib import parse

__all__ = ["AliSmsBase"]


class AliSmsBase(object):
    """
    阿里短信基础类
    """

    endpoint = "https://dysmsapi.aliyuncs.com/"

    def __init__(self, access_key: str, access_secret: str):
        self._app_key = access_key
        self._app_secret = access_secret

    def merge_args(self, args: dict, method: str = "POST") -> dict:
        d = {
            key: value
            for key, value in args.items()
            if value is not None and value != ""
        }

        # 添加公共请求参数
        # doc: https://help.aliyun.com/document_detail/101341.html
        t = datetime.utcfromtimestamp(int(time.time()))

        d["Format"] = "JSON"
        d["AccessKeyId"] = self._app_key
        d["SignatureMethod"] = "HMAC-SHA1"
        d["SignatureNonce"] = secrets.token_urlsafe(16)
        d["SignatureVersion"] = "1.0"
        d["Timestamp"] = f"{t.isoformat()}Z"
        d["Version"] = "2017-05-25"

        d["Signature"] = self._compute_signature(d, method, self._app_secret)

        return d

    @staticmethod
    def _compute_signature(d: dict, method: str, access_secret: str) -> str:
        """
        计算签名
            https://help.aliyun.com/document_detail/101343.html

        :param d:
        :param method: http method
        :param access_secret:
        :return:
        """

        # 2. 根据参数Key排序（顺序）
        # 3. 构造待签名的请求串
        sorted_params = sorted(d.items())
        t1 = parse.urlencode(sorted_params)
        t2 = parse.quote_plus(t1)

        data = f"{method}&%2F&{t2}"

        return AliSmsBase.compute_str_signature(data, access_secret + "&")

    @staticmethod
    def compute_str_signature(s: str, access_secret: str) -> str:
        signature = hmac.digest(access_secret.encode(), s.encode(), "sha1")
        return base64.b64encode(signature).decode()
