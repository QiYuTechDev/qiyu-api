from typing import List, Any

from pydantic import BaseModel


class BatchItemContentItem(BaseModel):
    code: str
    type_one_id: str
    tao_id: str
    title: str
    jianjie: str
    pict_url: str
    user_type: str
    seller_id: str
    shop_dsr: str
    volume: str
    size: str
    quanhou_jiage: str
    date_time_yongjin: str
    tkrate3: str
    yongjin_type: str
    coupon_id: str
    coupon_start_time: str
    coupon_end_time: str
    coupon_info_money: str
    coupon_total_count: str
    coupon_remain_count: str
    coupon_info: str
    juhuasuan: str
    taoqianggou: str
    haitao: str
    jiyoujia: str
    jinpaimaijia: str
    pinpai: str
    pinpai_name: str
    yunfeixian: str
    nick: str
    small_images: str
    white_image: str
    tao_title: str
    provcity: str
    shop_title: str
    zhibo_url: str
    sellCount: str
    commentCount: str
    favcount: str
    score1: str
    score2: str
    score3: str
    creditLevel: str
    shopIcon: str
    pcDescContent: str
    item_url: str
    category_id: str
    category_name: str
    level_one_category_id: str
    level_one_category_name: str
    tkfee3: str
    biaoqian: str
    tag: str
    date_time: str
    presale_discount_fee_text: str
    presale_tail_end_time: str
    presale_tail_start_time: str
    presale_end_time: str
    presale_start_time: str
    presale_deposit: str
    min_commission_rate: str


class BatchItemResp(BaseModel):
    status: int
    content: List[Any]
