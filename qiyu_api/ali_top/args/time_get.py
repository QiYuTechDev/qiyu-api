from pydantic import BaseModel, Field

__all__ = ["TimeGetArgs"]


class TimeGetArgs(BaseModel):
    """
    获取淘宝系统当前时间

    doc: https://open.taobao.com/api.htm?docId=120&docType=2
    """

    method: str = Field("taobao.time.get")
