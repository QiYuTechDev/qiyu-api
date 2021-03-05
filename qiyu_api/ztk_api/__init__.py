"""
折淘客 开放平台 API

官网: https://www.zhetaoke.com/
API接口: https://www.zhetaoke.com/user/extend/extend_lingquan_default.aspx
"""
from .auth_account_args import AuthAccountArgs  # noqa
from .bang_dan_tui_jian_args import BangDanTuiJianArgs  # noqa
from .batch_item_args import BatchItemsArgs  # noqa
from .batch_item_model import BatchItemModel  # noqa
from .batch_item_resp import BatchItemResp  # noqa
from .channel_account_info_args import ChannelAccountInfoArgs  # noqa
from .channel_id_list_args import ChannelIdListArgs  # noqa
from .channel_invite_code_args import ChannelInviteCodeArgs  # noqa
from .channel_save_record_args import ChannelSaveRecordArgs  # noqa
from .gao_yong_args import GaoYongArgs  # noqa
from .guess_you_like_args import GuessYouLikeArgs  # noqa
from .item_detail_args import ItemDetailArgs  # noqa
from .item_detail_model import ItemDetailModel  # noqa
from .item_detail_v2_args import ItemDetailV2Args  # noqa
from .item_detail_v2_model import ItemDetailV2Model  # noqa
from .item_detail_v2_resp import ItemDetailV2Resp  # noqa
from .ju_hua_suan_args import JuHuaSuanArgs  # noqa
from .new_order_args import NewOrderArgs  # noqa
from .nine_nine_args import NineNineArgs  # noqa
from .order_details_resp import OrderDetailsResp, OrderDto, TkStatusEnum  # noqa
from .search_args import SearchArgs  # noqa
from .suggest_args import SuggestArgs  # noqa
from .tkl_create_args import TKLCreateArgs  # noqa
from .tkl_create_resp import TKLCreateResp  # noqa
from .tmall_chao_shi_args import TMallChaoShiArgs  # noqa
from .tmall_shang_pin_args import TMallShangPinArgs  # noqa
from .ztk import ZTK  # noqa
from .ztk_std import ZTKStd  # noqa
from .ztk_sync import ZTKSync  # noqa
