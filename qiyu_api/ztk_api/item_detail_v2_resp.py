# 这个文件是由 json_code_gen_resp.py 自动生成的 请不要修改
from typing import List, Any

from pydantic import BaseModel


class ItemDetailV2Resp(BaseModel):
    status: int
    content: List[Any]
