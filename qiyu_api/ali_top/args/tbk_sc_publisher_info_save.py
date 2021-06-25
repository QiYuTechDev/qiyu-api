from typing import Optional

from pydantic import BaseModel, Field

__all__ = ["TBKScPublisherInfoSaveArgs"]


class TBKScPublisherInfoSaveArgs(BaseModel):
    """
    淘宝客-公用-私域用户备案

    doc: https://open.taobao.com/api.htm?docId=37988&docType=2
    """

    session: str = Field(
        None,
        title="用户登录授权成功后，TOP颁发给应用的授权信息",
        description="""
当此API的标签上注明：“需要授权”，则此参数必传；
“不需要授权”，则此参数不需要传；“可选授权”，则此参数为可选
""",
    )

    inviter_code: str = Field(..., title=" 渠道备案 - 淘宝客邀请渠道的邀请码")

    info_type: int = Field(1, title="类型，必选 默认为1:")

    target_app_key: Optional[str] = Field(
        None, title="被调用的目标AppKey，仅当被调用的API为第三方ISV提供时有效"
    )
    partner_id: Optional[str] = Field(None, title="合作伙伴身份标识")

    ###########################################
    relation_from: Optional[str] = Field(None, title="渠道备案 - 来源，取链接的来源")

    offline_scene: Optional[int] = Field(
        None, title="渠道备案 - 线下场景信息，1 - 门店，2- 学校，3 - 工厂，4 - 其他"
    )

    online_scene: Optional[int] = Field(
        None, title="渠道备案 - 线上场景信息，1 - 微信群，2- QQ群，3 - 其他"
    )

    note: Optional[str] = Field(None, title="媒体侧渠道备注")

    register_info: Optional[str] = Field(
        None,
        title="线下备案注册信息",
        description="""
    # 线下备案注册信息,字段包含:
    # 电话号码(phoneNumber，必填)
    # 省(province,必填)
    # 市(city,必填)
    # 区县街道(location,必填)
    # 详细地址(detailAddress,必填)
    # 经营类型(career,线下个人必填)
    # 店铺类型(shopType,线下店铺必填)
    # 店铺名称(shopName,线下店铺必填)
    # 店铺证书类型(shopCertifyType,线下店铺选填)
    # 店铺证书编号(certifyNumber,线下店铺选填)
    """,
    )

    simplify: bool = Field(
        False, title="是否采用精简JSON返回格式", description="仅当format=json时有效，默认值为：false"
    )

    method: str = Field("taobao.tbk.sc.publisher.info.save")
