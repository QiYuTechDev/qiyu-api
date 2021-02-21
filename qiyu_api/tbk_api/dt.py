from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

__all__ = ["TbkItemInfo", "TbkBrandInfo"]


class TbkBrandInfo(BaseModel):
    """
    品牌信息
    """

    brand_id: str = Field(..., title="品牌ID")
    brand_name: str = Field(..., title="品牌名称")
    brand_logo: str = Field(..., title="品牌logo", description="图片的URL")
    brand_desc: str = Field("", title="品牌介绍")

    sales_2h: int = Field(0, title="近期销量", description="也就是两小时之内的销量")


class TbkItemInfo(BaseModel):
    """
    淘宝商品信息
    """

    tao_id: str = Field(..., title="商品ID")
    tao_img: str = Field(..., title="商品主图")
    tao_link: Optional[str] = Field(None, title="商品链接")
    tao_details: List[str] = Field([], title="商品详情图", description="多个商品详情的链接")

    title_long: str = Field(..., title="淘宝标题")
    title_short: str = Field(..., title="短标题")

    price_origin: float = Field(..., title="商品原价")
    price_actual: float = Field(..., title="券后价")
    price_coupon: float = Field(0, title="优惠券金额")

    seller_id: Optional[str] = Field(None, title="卖家ID")
    seller_name: Optional[str] = Field(None, title="卖家名称")
    seller_logo: Optional[str] = Field(None, title="卖家图标")
    seller_level: Optional[int] = Field(None, title="淘宝店铺等级")

    score_dsr: Optional[float] = Field(None, title="描述评级")
    score_ship: Optional[float] = Field(None, title="物流服务")
    score_service: Optional[float] = Field(None, title="卖家服务评级")

    percent_dsr: Optional[float] = Field(None, title="卖家描述同行比")
    percent_ship: Optional[float] = Field(None, title="物流同行比")
    percent_service: Optional[float] = Field(None, title="卖家服务同行比")

    commission_rate: Optional[float] = Field(
        None, title="佣金比例", description="佣金比例: 在 0~1 之间 表示百分比"
    )
    commission_money: Optional[float] = Field(None, title="预估佣金")

    sale_month: int = Field(0, title="月销量")
    sale_day: int = Field(0, title="日销量")
    sale_two_hours: int = Field(0, title="两小时销量")

    coupon_start_time: Optional[datetime] = Field(None, title="优惠券开始时间")
    coupon_end_time: Optional[datetime] = Field(None, title="优惠券结束时间")
    coupon_total_num: Optional[int] = Field(None, title="优惠券总量")
    coupon_recv_num: Optional[int] = Field(None, title="优惠券领取量")
    coupon_link: Optional[str] = Field(None, title="优惠券链接")

    yun_fei_xian: Optional[bool] = Field(None, title="运费险")
