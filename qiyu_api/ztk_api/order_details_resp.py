from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional, Any, List

from dataclasses_json import DataClassJsonMixin

__all__ = ["OrderDetailsResp", "OrderDto", "TkStatusEnum"]


class TkStatusEnum(object):
    done = 3  # 订单结算
    paid = 12  # 订单付款
    cancel = 13  # 订单失效
    success = 14  # 确认收货


@dataclass
class OrderDto(DataClassJsonMixin):
    # 订单在淘宝拍下付款的时间
    tb_paid_time: Optional[str] = None
    # 订单付款的时间，该时间同步淘宝，可能会略晚于买家在淘宝的订单创建时间
    tk_paid_time: Optional[str] = None
    # 买家确认收货的付款金额（不包含运费金额）
    # 这个大概率 是空字段 使用 alipay_total_price
    pay_price: Optional[str] = None
    # 结算预估收入 = 结算金额*提成。
    # 以买家确认收货的付款金额为基数，预估您可能获得的收入。
    # 因买家退款、您违规推广等原因，可能与您最终收入不一致。最终收入以月结后您实际收到的为准
    pub_share_fee: Optional[str] = None
    # 买家通过购物车购买的每个商品对应的订单编号，此订单编号并未在淘宝买家后台透出
    trade_id: Optional[str] = None
    # 二方：佣金收益的第一归属者； 三方：从其他淘宝客佣金中进行分成的推广者
    tk_order_role: Optional[int] = None
    # 订单确认收货后且商家完成佣金支付的时间
    tk_earning_time: Optional[str] = None
    # 推广位管理下的推广位名称对应的ID，同时也是pid=mm_1_2_3中的“3”这段数字
    adzone_id: Optional[str] = None
    # 从结算佣金中分得的收益比率
    pub_share_rate: Optional[str] = None
    # 维权标签，0 含义为非维权 1 含义为维权订单
    refund_tag: Optional[int] = None
    # 平台给与的补贴比率，如天猫、淘宝、聚划算等
    subsidy_rate: Optional[str] = None
    # 提成=收入比率*分成比率。指实际获得收益的比率
    tk_total_rate: Optional[str] = None
    # 商品所属的根类目，即一级类目的名称
    item_category_name: Optional[str] = None
    # 商家昵称
    seller_nick: Optional[str] = None
    # 推广者的会员id
    pub_id: Optional[int] = None
    # 推广者赚取佣金后支付给阿里妈妈的技术服务费用的比率
    alimama_rate: Optional[str] = None
    # 平台出资方，如天猫、淘宝、或聚划算等
    subsidy_type: Optional[str] = None
    # 商品图片
    item_img: Optional[str] = None
    # 付款预估收入=付款金额*提成。
    # 指买家付款金额为基数，预估您可能获得的收入。
    # 因买家退款等原因，可能与结算预估收入不一致
    pub_share_pre_fee: Optional[str] = None
    # 支付总额 买家拍下付款的金额（不包含运费金额）
    alipay_total_price: Optional[str] = None
    # 商品标题
    item_title: Optional[str] = None
    # 媒体管理下的对应ID的自定义名称
    site_name: Optional[str] = None
    # 商品数量
    item_num: Optional[int] = None
    # 补贴金额=结算金额*补贴比率
    subsidy_fee: Optional[str] = None
    # 技术服务费=结算金额*收入比率*技术服务费率。
    # 推广者赚取佣金后支付给阿里妈妈的技术服务费用
    alimama_share_fee: Optional[str] = None
    # 交易父 ID 买家在淘宝后台显示的订单编号
    # [用户可以看到的订单号码]
    trade_parent_id: Optional[str] = None
    # 订单所属平台类型，包括天猫、淘宝、聚划算等
    order_type: Optional[str] = None
    # 订单创建的时间，该时间同步淘宝，可能会略晚于买家在淘宝的订单创建时间
    tk_create_time: Optional[str] = None
    # 产品类型
    flow_source: Optional[str] = None
    # 成交平台
    terminal_type: Optional[str] = None
    # 通过推广链接达到商品、店铺详情页的点击时间
    click_time: Optional[str] = None
    # 淘宝客 状态
    # 已付款：指订单已付款，但还未确认收货
    # 已收货：指订单已确认收货，但商家佣金未支付
    # 已结算：指订单已确认收货，且商家佣金已支付成功
    # 已失效：指订单关闭/订单佣金小于0.01元，
    #   订单关闭主要有：
    #   1）买家超时未付款；
    #   2）买家付款前，买家/卖家取消了订单；
    #   3）订单付款后发起售中退款成功；
    #
    # 取值:
    #  3：订单结算，结算成功 [说明淘宝已经给这个订单结算了]
    # 12：订单付款， [用户已经付款]
    # 13：订单失效， [订单被取消 等]
    # 14：订单成功/确认收货
    tk_status: Optional[int] = None
    # 商品单价
    item_price: Optional[str] = None
    # 商品id
    item_id: Optional[int] = None
    # 推广位管理下的自定义推广位名称
    adzone_name: Optional[str] = None
    # 佣金比率
    total_commission_rate: Optional[str] = None
    # 商品的 URL 商品链接
    item_link: Optional[str] = None
    # 媒体管理下的ID，同时也是pid=mm_1_2_3中的“2”这段数字
    site_id: Optional[int] = None
    # 店铺名称
    seller_shop_title: Optional[str] = None
    # 订单结算的佣金比率+平台的补贴比率
    income_rate: Optional[str] = None
    # 佣金金额=结算金额＊佣金比率
    total_commission_fee: Optional[str] = None
    # 预估内容专项服务费：
    #   内容场景专项技术服务费，内容推广者在内容场景进行推广需要支付给阿里妈妈专项的技术服务费用。
    # 专项服务费＝付款金额＊专项服务费率。
    tk_commission_pre_fee_for_media_platform: Optional[str] = None
    # 结算内容专项服务费：
    #   内容场景专项技术服务费，内容推广者在内容场景进行推广需要支付给阿里妈妈专项的技术服务费用。
    # 专项服务费＝结算金额＊专项服务费率。
    tk_commission_fee_for_media_platform: Optional[str] = None
    # 内容专项服务费率：
    #   内容场景专项技术服务费率，
    #   内容推广者在内容场景进行推广需要按结算金额支付一定比例给阿里妈妈作为内容场景专项技术服务费，
    #   用于提供与内容平台实现产品技术对接等服务。
    tk_commission_rate_for_media_platform: Optional[str] = None
    # 会员运营id
    special_id: Optional[int] = None
    # 渠道关系id
    relation_id: Optional[int] = None
    # 预售时期，用户对预售商品支付定金的付款时间，可能略晚于在淘宝付定金时间
    tk_deposit_time: Optional[str] = None
    # 预售时期，用户对预售商品支付定金的付款时间
    tb_deposit_time: Optional[str] = None
    # 预售时期，用户对预售商品支付的定金金额
    deposit_price: Optional[str] = None
    # 开发者调用api的appkey
    app_key: Optional[str] = None
    # 口碑子订单号
    alsc_id: Optional[str] = None
    # 口碑父订单号
    alsc_pid: Optional[str] = None
    # 服务费信息
    service_fee_dto_list: Optional[Any] = None
    # 激励池对应的rid
    lx_rid: Optional[str] = None
    # 订单是否为激励池订单 1，表征是 0，表征否
    is_lx: Optional[str] = None

    def ali_pay_price(self) -> Optional[Decimal]:
        if self.alipay_total_price is None:
            return None
        return Decimal(self.alipay_total_price)

    def income(self) -> Optional[Decimal]:
        if self.pub_share_fee is not None:
            ret = Decimal(self.pub_share_fee)
            if ret >= 0.01:
                return ret

        if self.pub_share_pre_fee is None:
            return Decimal(0)
        return Decimal(self.pub_share_pre_fee)

    def order_ctime(self) -> Optional[datetime]:
        return self._str_to_datetime(self.tk_create_time)

    def end_time(self) -> Optional[datetime]:
        return self._str_to_datetime(self.tk_earning_time)

    def pay_time(self) -> Optional[datetime]:
        return self._str_to_datetime(self.tk_paid_time)

    @staticmethod
    def _str_to_datetime(s: Optional[str]) -> Optional[datetime]:
        if s is None:
            return None

        try:
            return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return None

    def order_platform(self) -> str:
        """
        获取订单的平台
        """
        if self.order_type is None:
            return "--"
        else:
            return self.order_type

    def is_order_canceled(self) -> bool:
        """
        订单失效/取消
        """
        return self.tk_status == TkStatusEnum.cancel

    def is_order_paid(self) -> bool:
        """
        订单已经付款
        """
        return self.tk_status == TkStatusEnum.paid

    def is_order_success(self) -> bool:
        """
        已经收货
        """
        return self.tk_status == TkStatusEnum.success

    def is_order_done(self) -> bool:
        """
        已经结算
        """
        return self.tk_status == TkStatusEnum.done


@dataclass
class OrderDetailsResp(DataClassJsonMixin):
    has_next: bool
    has_pre: bool
    page_no: int
    page_size: int
    position_index: str
    # use get_order_lists 获取订单列表
    results: Optional[dict]

    @staticmethod
    def from_result(j: dict) -> Optional["OrderDetailsResp"]:
        resp = j["tbk_sc_order_details_get_response"]
        if "data" not in resp:
            return None

        data = resp["data"]
        if not isinstance(data, dict):
            return None

        if len(data["results"]) == 0:
            data["results"] = None

        return OrderDetailsResp.from_dict(data)

    def get_order_lists(self) -> List[OrderDto]:
        if not isinstance(self.results, dict):
            return []

        order_list = []
        if "publisher_order_dto" in self.results:
            order_list = self.results["publisher_order_dto"]

        return list(map(lambda x: OrderDto.from_dict(x), order_list))
