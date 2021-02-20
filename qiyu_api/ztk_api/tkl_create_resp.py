from dataclasses import dataclass
from typing import Optional

from dataclasses_json import DataClassJsonMixin


@dataclass
class TKLCreateResp(DataClassJsonMixin):
    """
    参见: https://www.zhetaoke.com/user/open/open_tkl_create.aspx
    参见: https://open.taobao.com/api.htm?docId=31127&docType=2
    """

    #  iOS 14 版本的淘口令
    model: Optional[str] = None
    #  iOS 14 版本的淘口令
    password_simple: Optional[str] = None

    status: Optional[int] = None
    content: Optional[str] = None

    def is_success(self):
        if self.model is not None:
            return True
        return False
