from dataclasses import dataclass
from typing import List, Optional

from dataclasses_json import DataClassJsonMixin


class HTTPValidationError(object):
    # Detail
    detail: Optional[List["ValidationError"]] = None


@dataclass
class PushForm(DataClassJsonMixin):
    # iOS 设备的 token
    # HEX 编码的 iOS 设备的token
    token: str
    # 内容
    # 推送给客户端的内容
    content: str
    # 角标数量
    # 客户端显示的角标的数量
    badge: Optional[int] = 0
    # 推送分类
    # 客户端推送的分类
    category: Optional[str] = None
    # sandbox 环境
    # 是否使用 sandbox 环境
    sandbox: Optional[bool] = False


class ValidationError(object):
    # Location
    loc: List[str]
    # Message
    msg: str
    # Error Type
    type: str
