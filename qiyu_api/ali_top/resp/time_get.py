from pydantic import BaseModel, Field

__all__ = ["TimeGetResp"]


class TimeGetResp(BaseModel):
    """
    获取淘宝系统当前时间

    doc: https://open.taobao.com/api.htm?docId=120&docType=2
    """

    time: str = Field(..., title="时间")
    request_id: str = Field(..., title="请求ID")
