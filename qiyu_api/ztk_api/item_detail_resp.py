from dataclasses import dataclass
from typing import Optional, Dict, List

from dataclasses_json import DataClassJsonMixin


@dataclass
class ItemDetailResp(DataClassJsonMixin):
    """
    商品详情返回信息
    """

    cat_leaf_name: str
    cat_name: str
    item_url: str
    ju_online_end_time: str
    ju_online_start_time: str
    ju_pre_show_end_time: str
    ju_pre_show_start_time: str
    material_lib_type: str
    nick: str
    num_iid: str
    pict_url: str
    presale_deposit: str
    presale_end_time: str
    presale_start_time: str
    presale_tail_end_time: str
    presale_tail_start_time: str
    provcity: str
    reserve_price: str
    seller_id: str
    small_images: Dict[str, Optional[List[str]]]
    title: str
    tmall_play_activity_end_time: int
    tmall_play_activity_start_time: int
    user_type: int
    volume: int
    zk_final_price: str
    kuadian_promotion_info: Optional[str] = None

    @staticmethod
    def from_ztk_resp(j: dict) -> Optional["ItemDetailResp"]:
        if "tbk_item_info_get_response" not in j:
            return None
        j = j["tbk_item_info_get_response"]

        if "results" not in j:
            return None
        j = j["results"]

        if "n_tbk_item" not in j:
            return None
        j = j["n_tbk_item"]

        if isinstance(j, list) and len(j) >= 1:
            return ItemDetailResp(**j[0])
        else:
            return None
