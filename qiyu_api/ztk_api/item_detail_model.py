from typing import Optional, Dict, List

from pydantic import BaseModel

from . import fields


class ItemDetailModel(BaseModel):
    """
    商品详情返回信息
    """

    cat_leaf_name: str = fields.cat_leaf_name_field
    cat_name: str = fields.cat_name_field
    item_url: str = fields.item_url_field
    ju_online_end_time: str = fields.ju_online_end_time_field
    ju_online_start_time: str = fields.ju_online_start_time_field
    ju_pre_show_end_time: str = fields.ju_pre_show_end_time_field
    ju_pre_show_start_time: str = fields.ju_pre_show_start_time_field
    material_lib_type: str = fields.material_lib_type_field
    nick: str = fields.nick_field
    num_iid: str = fields.num_iid_field
    pict_url: str = fields.pict_url_field
    presale_deposit: str = fields.presale_deposit_field
    presale_end_time: str = fields.presale_end_time_field
    presale_start_time: str = fields.presale_start_time_field
    presale_tail_end_time: str = fields.presale_tail_end_time_field
    presale_tail_start_time: str = fields.presale_tail_start_time_field
    provcity: str = fields.provcity_field
    reserve_price: str = fields.reserve_price_field
    seller_id: str = fields.seller_id_field
    small_images: Dict[str, Optional[List[str]]] = fields.small_images_field
    title: str = fields.title_field
    tmall_play_activity_end_time: int = fields.tmall_play_activity_end_time_field
    tmall_play_activity_start_time: int = fields.tmall_play_activity_start_time_field
    user_type: int = fields.user_type_field
    volume: int = fields.volume_field
    zk_final_price: str = fields.zk_final_price_field
    kuadian_promotion_info: Optional[str] = fields.kuadian_promotion_info_field
