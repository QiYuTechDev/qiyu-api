from typing import Optional

from pydantic import BaseModel, Field

__all__ = ["TopAuthTokenCreateArgs"]


class TopAuthTokenCreateArgs(BaseModel):
    """
    获取Access Token

    doc: https://open.taobao.com/api.htm?docId=25388&docType=2
    """

    code: Optional[str] = Field(None, title="授权code，grantType==authorization_code 时需要")

    uuid: Optional[str] = Field(None, title="与生成code的uuid配对")

    method: str = Field("taobao.top.auth.token.create", title="固定值")
