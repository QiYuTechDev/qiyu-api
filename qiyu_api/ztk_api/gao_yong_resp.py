from typing import List, Any

from pydantic import BaseModel, Field


class GaoYongContentItem(BaseModel):
    code: str = Field(None)
    type_one_id: str = Field(None)
    tao_id: str = Field(None)
    title: str = Field(None)
    jianjie: str = Field(None)
    pict_url: str = Field(None)
    user_type: str = Field(None)
    seller_id: str = Field(None)
    shop_dsr: str = Field(None)
    volume: str = Field(None)
    size: str = Field(None)
    quanhou_jiage: str = Field(None)
    date_time_yongjin: str = Field(None)
    tkrate3: str = Field(None)
    yongjin_type: str = Field(None)
    coupon_id: str = Field(None)
    coupon_start_time: str = Field(None)
    coupon_end_time: str = Field(None)
    coupon_info_money: str = Field(None)
    coupon_total_count: str = Field(None)
    coupon_remain_count: str = Field(None)
    coupon_info: str = Field(None)
    juhuasuan: str = Field(None)
    taoqianggou: str = Field(None)
    haitao: str = Field(None)
    jiyoujia: str = Field(None)
    jinpaimaijia: str = Field(None)
    pinpai: str = Field(None)
    pinpai_name: str = Field(None)
    yunfeixian: str = Field(None)
    nick: str = Field(None)
    small_images: str = Field(None)
    white_image: str = Field(None)
    tao_title: str = Field(None)
    provcity: str = Field(None)
    shop_title: str = Field(None)
    zhibo_url: str = Field(None)
    sellCount: str = Field(None)
    commentCount: str = Field(None)
    favcount: str = Field(None)
    score1: str = Field(None)
    score2: str = Field(None)
    score3: str = Field(None)
    creditLevel: str = Field(None)
    shopIcon: str = Field(None)
    pcDescContent: str = Field(None)
    taobao_url: str = Field(None)
    category_id: str = Field(None)
    category_name: str = Field(None)
    level_one_category_id: str = Field(None)
    level_one_category_name: str = Field(None)
    tkfee3: str = Field(None)
    biaoqian: str = Field(None)
    tag: str = Field(None)
    date_time: str = Field(None)
    presale_discount_fee_text: str = Field(None)
    presale_tail_end_time: str = Field(None)
    presale_tail_start_time: str = Field(None)
    presale_end_time: str = Field(None)
    presale_start_time: str = Field(None)
    presale_deposit: str = Field(None)
    min_commission_rate: str = Field(None)
    coupon_click_url: str = Field(None)
    item_url: str = Field(None)
    shorturl: str = Field(None)
    tkl: str = Field(None)


class GaoYongResp(BaseModel):
    status: int
    content: List[Any]
