# 这个文件是由 json_code_gen_resp.py 自动生成的 请不要修改
from dataclasses import dataclass
from typing import List, Any

from dataclasses_json import DataClassJsonMixin


@dataclass
class ItemDetailV2Resp(DataClassJsonMixin):
    status: int
    content: List[Any]
