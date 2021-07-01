from typing import List, Dict

from pydantic import BaseModel, Field

__all__ = ["UserSellerGetArgs"]


class UserSellerGetArgs(BaseModel):
    """
    查询卖家用户信息

    doc: https://open.taobao.com/api.htm?docId=21349&docType=2
    """

    session: str = Field(..., title="session key")
    fields: List[str] = Field(None, title="需要返回的字段列表，可选值为返回示例值中的可以看到的字段")
    method: str = Field("taobao.user.seller.get", title="固定值")

    def to_dict(self) -> Dict[str, str]:
        d = self.dict()
        d["fields"] = ",".join(d["fields"])
        return d
