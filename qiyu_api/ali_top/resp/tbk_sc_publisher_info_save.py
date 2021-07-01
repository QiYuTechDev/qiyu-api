from typing import Optional

from pydantic import Field, BaseModel

__all__ = ["TBKScPublisherInfoSaveResp"]


class TBKScPublisherInfoSaveResp(BaseModel):
    """
    淘宝客-公用-私域用户备案

    doc: https://open.taobao.com/api.htm?docId=37988&docType=2
    """

    account_name: str = Field(..., title="渠道昵称")
    desc: str = Field(..., title="如果重复绑定会提示：”重复绑定渠道“或”重复绑定粉丝“")
    relation_id: Optional[int] = Field(None, title="渠道关系ID")
    special_id: Optional[int] = Field(None, title="会员运营ID")
