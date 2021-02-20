from typing import List

from pydantic import BaseModel, Field


class GenericItemInfo(BaseModel):
    id: int = Field(..., title="")
    goodsId: str = Field(..., title="")
    title: str = Field(..., title="")
    dtitle: str = Field(..., title="")
    originalPrice: float = Field(..., title="")
    actualPrice: float = Field(..., title="")
    shopType: int = Field(..., title="")
    goldSellers: int = Field(..., title="")
    monthSales: int = Field(..., title="")
    twoHoursSales: int = Field(..., title="")
    dailySales: int = Field(..., title="")
    commissionType: int = Field(..., title="")
    desc: str = Field(..., title="")
    couponReceiveNum: int = Field(..., title="")
    couponLink: str = Field(..., title="")
    couponEndTime: str = Field(..., title="")
    couponStartTime: str = Field(..., title="")
    couponPrice: float = Field(..., title="")
    couponConditions: str = Field(..., title="")
    activityType: int = Field(..., title="")
    createTime: str = Field(..., title="")
    mainPic: str = Field(..., title="")
    marketingMainPic: str = Field(..., title="")
    sellerId: str = Field(..., title="")
    cid: int = Field(..., title="")
    discounts: float = Field(..., title="")
    commissionRate: float = Field(..., title="")
    couponTotalNum: int = Field(..., title="")
    haitao: int = Field(..., title="")
    activityStartTime: str = Field(..., title="")
    activityEndTime: str = Field(..., title="")
    shopName: str = Field(..., title="")
    shopLevel: int = Field(..., title="")
    descScore: float = Field(..., title="")
    brand: int = Field(..., title="")
    brandId: int = Field(..., title="")
    brandName: str = Field(..., title="")
    hotPush: int = Field(..., title="")
    teamName: str = Field(..., title="")
    itemLink: str = Field(..., title="")
    tchaoshi: int = Field(..., title="")

    dsrScore: float = Field(..., title="")
    dsrPercent: float = Field(..., title="")

    shipScore: float = Field(..., title="")
    shipPercent: float = Field(..., title="")

    serviceScore: float = Field(..., title="")
    servicePercent: float = Field(..., title="")

    subcid: List[int] = Field(..., title="")
    nineCid: int = Field(..., title="")
    quanMLink: int = Field(..., title="")
    hzQuanOver: int = Field(..., title="")
    yunfeixian: int = Field(..., title="")
    estimateAmount: int = Field(..., title="")
    freeshipRemoteDistrict: int = Field(..., title="")
    video: str = Field(..., title="")
    tbcid: int = Field(..., title="")


class GenericData(BaseModel):
    list: List[GenericItemInfo] = Field(..., title="")
    totalNum: int = Field(..., title="")
    pageId: str = Field(..., title="")


class GenericResp(BaseModel):
    time: int = Field(..., title="")
    code: int = Field(..., title="")
    msg: str = Field(..., title="")
    data: GenericData = Field(..., title="")
