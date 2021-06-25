from typing import List, Dict, Optional

from pydantic import BaseModel, Field

__all__ = ["ProductGetArgs"]


class ProductGetArgs(BaseModel):
    """
    获取一个产品的信息

    doc: https://open.taobao.com/api.htm?docId=4&docType=2
    """

    product_id: Optional[int] = Field(
        None,
        title="Product的id",
        description="""
    两种方式来查看一个产品:
    1.传入product_id来查询
    2.传入cid和props来查询
    """,
    )

    cid: Optional[int] = Field(
        None,
        title="商品类目id",
        description="""

    调用taobao.itemcats.get获取;
    必须是叶子类目id,
    如果没有传product_id,那么cid和props必须要传.
    """,
    )

    #
    props: Optional[int] = Field(
        None,
        title="诺基亚N73这个产品的关键属性列表",
        description="品牌:诺基亚;型号:N73,对应的PV值就是10005:10027;10006:29729.",
    )

    method: str = Field("taobao.product.get", title="固定值")

    # 需要返回的字段列表，可选值为返回示例值中的可以看到的字段
    fields: List[str] = ("name", "binds", "product_id")

    def to_dict(self) -> Dict[str, str]:
        d = self.dict()
        d["fields"] = ",".join(d["fields"])
        return d
