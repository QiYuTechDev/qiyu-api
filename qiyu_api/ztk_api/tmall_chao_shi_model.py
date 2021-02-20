# 这个文件是由 json_code_gen_model.py 自动生成的 请不要修改

from typing import Optional

from pydantic import BaseModel

from . import fields


class TmallChaoShiModel(BaseModel):
    code: Optional[str] = fields.code_field
    type_one_id: Optional[str] = fields.type_one_id_field
    tao_id: Optional[str] = fields.tao_id_field
    title: Optional[str] = fields.title_field
    jianjie: Optional[str] = fields.jianjie_field
    pict_url: Optional[str] = fields.pict_url_field
    user_type: Optional[str] = fields.user_type_field
    seller_id: Optional[str] = fields.seller_id_field
    shop_dsr: Optional[str] = fields.shop_dsr_field
    volume: Optional[str] = fields.volume_field
    size: Optional[str] = fields.size_field
    quanhou_jiage: Optional[str] = fields.quanhou_jiage_field
    date_time_yongjin: Optional[str] = fields.date_time_yongjin_field
    tkrate3: Optional[str] = fields.tkrate3_field
    yongjin_type: Optional[str] = fields.yongjin_type_field
    coupon_id: Optional[str] = fields.coupon_id_field
    coupon_start_time: Optional[str] = fields.coupon_start_time_field
    coupon_end_time: Optional[str] = fields.coupon_end_time_field
    coupon_info_money: Optional[str] = fields.coupon_info_money_field
    coupon_total_count: Optional[str] = fields.coupon_total_count_field
    coupon_remain_count: Optional[str] = fields.coupon_remain_count_field
    coupon_info: Optional[str] = fields.coupon_info_field
    juhuasuan: Optional[str] = fields.juhuasuan_field
    taoqianggou: Optional[str] = fields.taoqianggou_field
    haitao: Optional[str] = fields.haitao_field
    jiyoujia: Optional[str] = fields.jiyoujia_field
    jinpaimaijia: Optional[str] = fields.jinpaimaijia_field
    pinpai: Optional[str] = fields.pinpai_field
    pinpai_name: Optional[str] = fields.pinpai_name_field
    yunfeixian: Optional[str] = fields.yunfeixian_field
    nick: Optional[str] = fields.nick_field
    small_images: Optional[str] = fields.small_images_field
    white_image: Optional[str] = fields.white_image_field
    tao_title: Optional[str] = fields.tao_title_field
    provcity: Optional[str] = fields.provcity_field
    shop_title: Optional[str] = fields.shop_title_field
    zhibo_url: Optional[str] = fields.zhibo_url_field
    sellCount: Optional[str] = fields.sellCount_field
    commentCount: Optional[str] = fields.commentCount_field
    favcount: Optional[str] = fields.favcount_field
    score1: Optional[str] = fields.score1_field
    score2: Optional[str] = fields.score2_field
    score3: Optional[str] = fields.score3_field
    creditLevel: Optional[str] = fields.creditLevel_field
    shopIcon: Optional[str] = fields.shopIcon_field
    pcDescContent: Optional[str] = fields.pcDescContent_field
    item_url: Optional[str] = fields.item_url_field
    category_id: Optional[str] = fields.category_id_field
    category_name: Optional[str] = fields.category_name_field
    level_one_category_id: Optional[str] = fields.level_one_category_id_field
    level_one_category_name: Optional[str] = fields.level_one_category_name_field
    tkfee3: Optional[str] = fields.tkfee3_field
    biaoqian: Optional[str] = fields.biaoqian_field
    tag: Optional[str] = fields.tag_field
    presale_discount_fee_text: Optional[str] = fields.presale_discount_fee_text_field
    presale_tail_end_time: Optional[str] = fields.presale_tail_end_time_field
    presale_tail_start_time: Optional[str] = fields.presale_tail_start_time_field
    presale_end_time: Optional[str] = fields.presale_end_time_field
    presale_start_time: Optional[str] = fields.presale_start_time_field
    presale_deposit: Optional[str] = fields.presale_deposit_field
