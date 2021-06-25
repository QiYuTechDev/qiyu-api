from pydantic import BaseModel, Field

__all__ = ["TopAuthTokenCreateResp"]


class TopAuthTokenCreateResp(BaseModel):
    """
    获取Access Token

    doc: https://open.taobao.com/api.htm?docId=25388&docType=2
    """

    token_result: str = Field(
        ...,
        title="返回的是json信息",
        description="""
    和之前调用
    https://oauth.taobao.com/tac/token
    https://oauth.alibaba.com/token
    换token返回的字段信息一致

    参见: dt.TopAuthTokenCreateTokenResult
    """,
    )
