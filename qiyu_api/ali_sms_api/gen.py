from typing import Optional, List
from urllib import parse

import requests
from aiohttp import ClientSession, ClientResponse
from pydantic import BaseModel, Field

from .base import AliSmsBase


class QuerySendDetailsQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    # 例子: 15900000000
    PhoneNumber: str = Field(
        ...,
        title=f"""接收短信的手机号码。

格式：
* 国内短信：11位手机号码，例如15900000000。
* 国际/港澳台消息：国际区号+号码，例如85200000000。
""",
    )

    # 例子: 20181228
    SendDate: str = Field(
        ...,
        title=f"""短信发送日期，支持查询最近30天的记录。

格式为yyyyMMdd，例如20181225。""",
    )

    # 例子: 10
    PageSize: int = Field(
        ...,
        title=f"""分页查看发送记录，指定每页显示的短信记录数量。

取值范围为1~50。""",
    )

    # 例子: 1
    CurrentPage: int = Field(..., title=f"""分页查看发送记录，指定发送记录的的当前页码。""")

    # 例子: 155780923770
    OwnerId: Optional[int] = Field(None, title=f"""RAM用户的虚拟账号ID。""")

    # 例子: 134523^4351232
    BizId: Optional[str] = Field(
        None, title=f"""发送回执ID，即发送流水号。调用发送接口SendSms或SendBatchSms发送短信时，返回值中的BizId字段。"""
    )

    Action: str = Field("QuerySendDetails", title="系统的Action")


class SendBatchSmsQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    # 例子: ["15900000000","13500000000"]
    PhoneNumberJson: str = Field(
        ...,
        title=f"""接收短信的手机号码，JSON数组格式。

手机号码格式：
* 国内短信：11位手机号码，例如15900000000。
* 国际/港澳台消息：国际区号+号码，例如85200000000。

> 验证码类型短信，建议使用接口SendSms单独发送。""",
    )

    # 例子: ["阿里云","阿里巴巴"]
    SignNameJson: str = Field(
        ...,
        title=f"""短信签名名称，JSON数组格式。

请在控制台**签名管理**页面**签名名称**一列查看。

<note> 必须是已添加、并通过审核的短信签名；且短信签名的个数必须与手机号码的个数相同、内容一一对应。</note>""",
    )

    # 例子: SMS_152550005
    TemplateCode: str = Field(
        ...,
        title=f"""短信模板CODE。请在控制台**模板管理**页面**模板CODE**一列查看。

<note>必须是已添加、并通过审核的模板CODE；且发送国际/港澳台消息时，请使用国际/港澳台短信模版。</note>
""",
    )

    # 例子: 155780923770
    OwnerId: Optional[int] = Field(None, title=f"""RAM用户的虚拟账号ID。""")

    templateParamJson: Optional[str] = Field(None, title=f"""""")

    # 例子: [{"name":"TemplateParamJson"},{"name":"TemplateParamJson"}]
    TemplateParamJson: Optional[str] = Field(
        None,
        title=f"""短信模板变量对应的实际值，JSON格式。

<note>如果JSON中需要带换行符，请参照标准的JSON协议处理；且模板变量值的个数必须与手机号码、签名的个数相同、内容一一对应，表示向指定手机号码中发对应签名的短信，且短信模板中的变量参数替换为对应的值。</note>""",
    )

    # 例子: ["90999","90998"]
    SmsUpExtendCodeJson: Optional[str] = Field(
        None, title=f"""上行短信扩展码，JSON数组格式。无特殊需要此字段的用户请忽略此字段。"""
    )

    Action: str = Field("SendBatchSms", title="系统的Action")


class SendSmsQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    # 例子: 15900000000
    PhoneNumbers: str = Field(
        ...,
        title=f"""接收短信的手机号码。

格式：
* 国内短信：11位手机号码，例如15951955195。
* 国际/港澳台消息：国际区号+号码，例如85200000000。

支持对多个手机号码发送短信，手机号码之间以英文逗号（,）分隔。上限为1000个手机号码。批量调用相对于单条调用及时性稍有延迟。

<note>验证码类型短信，建议使用单独发送的方式。</note>""",
    )

    # 例子: 阿里云
    SignName: str = Field(
        ...,
        title=f"""短信签名名称。请在控制台**签名管理**页面**签名名称**一列查看。

<note>必须是已添加、并通过审核的短信签名。</note>""",
    )

    # 例子: SMS_153055065
    TemplateCode: str = Field(
        ...,
        title=f"""短信模板ID。请在控制台**模板管理**页面**模板CODE**一列查看。

<note>必须是已添加、并通过审核的短信签名；且发送国际/港澳台消息时，请使用国际/港澳台短信模版。</note>""",
    )

    # 例子: 155780923770
    OwnerId: Optional[int] = Field(None, title=f"""RAM用户的虚拟账号ID。""")

    # 例子: {"code":"1111"}
    TemplateParam: Optional[str] = Field(
        None,
        title=f"""短信模板变量对应的实际值，JSON格式。

<note>如果JSON中需要带换行符，请参照标准的JSON协议处理。</note>""",
    )

    # 例子: 90999
    SmsUpExtendCode: Optional[str] = Field(
        None, title=f"""上行短信扩展码，无特殊需要此字段的用户请忽略此字段。"""
    )

    # 例子: abcdefgh
    OutId: Optional[str] = Field(None, title=f"""外部流水扩展字段。""")

    Action: str = Field("SendSms", title="系统的Action")


class AddSmsSignSignFileListField(BaseModel):
    FileSuffix: str
    FileContents: str


class AddSmsSignQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    # 例子: 阿里云
    SignName: str = Field(
        ...,
        title=f"""签名名称。

> 签名必须符合[个人用户签名规范](~~108076~~)或[企业用户签名规范](~~108254~~)。""",
    )

    # 例子: 1
    SignSource: int = Field(
        ...,
        title=f"""签名来源。其中：

- 0：企事业单位的全称或简称。
- 1：工信部备案网站的全称或简称。
- 2：APP应用的全称或简称。
- 3：公众号或小程序的全称或简称。
- 4：电商平台店铺名的全称或简称。
- 5：商标名的全称或简称

> 签名来源为1时，请在申请说明中添加网站域名，加快审核速度。""",
    )

    # 例子: 当前的短信签名应用于双11大促推广营销
    Remark: str = Field(
        ...,
        title=f"""短信签名申请说明。请在申请说明中详细描述您的业务使用场景，申请工信部备案网站的全称或简称请在此处填写域名，长度不超过200个字符。""",
    )

    SignFileList: List[AddSmsSignSignFileListField] = Field(..., title=f"""""")

    # 例子: 155780923770
    OwnerId: Optional[int] = Field(None, title=f"""RAM用户的虚拟账号ID。""")

    Action: str = Field("AddSmsSign", title="系统的Action")


class DeleteSmsSignQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    # 例子: 阿里云
    SignName: str = Field(
        ...,
        title=f"""短信签名。

> 必须是本账号已申请的短信签名。""",
    )

    # 例子: 155780923770
    OwnerId: Optional[int] = Field(None, title=f"""RAM用户的虚拟账号ID。""")

    Action: str = Field("DeleteSmsSign", title="系统的Action")


class ModifySmsSignSignFileListField(BaseModel):
    FileSuffix: str
    FileContents: str


class ModifySmsSignQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    # 例子: 阿里云
    SignName: str = Field(
        ...,
        title=f"""签名内容。

> 签名内容必须符合[个人用户签名规范](~~108076~~)或[企业用户签名规范](~~108254~~)。""",
    )

    # 例子: 1
    SignSource: int = Field(
        ...,
        title=f"""签名来源。其中：

- 0：企事业单位的全称或简称。
- 1：工信部备案网站的全称或简称。
- 2：APP应用的全称或简称。
- 3：公众号或小程序的全称或简称。
- 4：电商平台店铺名的全称或简称。
- 5：商标名的全称或简称

> 签名来源为1时，请在申请说明中添加网站域名，加快审核速度。""",
    )

    # 例子: 当前的短信签名应用于双11大促推广营销
    Remark: str = Field(
        ...,
        title=f"""短信签名申请说明。请在申请说明中详细描述您的业务使用场景，申请工信部备案网站的全称或简称请在此处填写域名，长度不超过200个字符。""",
    )

    SignFileList: List[ModifySmsSignSignFileListField] = Field(..., title=f"""""")

    # 例子: 155780923770
    OwnerId: Optional[int] = Field(None, title=f"""RAM用户的虚拟账号ID。""")

    Action: str = Field("ModifySmsSign", title="系统的Action")


class AddSmsTemplateQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    # 例子: 1
    TemplateType: int = Field(
        ...,
        title=f"""短信类型。其中：
- 0：验证码。
- 1：短信通知。
- 2：推广短信。
- 3：国际/港澳台消息。""",
    )

    # 例子: 阿里云短信测试模板
    TemplateName: str = Field(..., title=f"""模板名称，长度为1~30个字符。""")

    # 例子: 您正在申请手机注册，验证码为：${code}，5分钟内有效！
    TemplateContent: str = Field(
        ...,
        title=f"""模板内容，长度为1~500个字符。

模板内容需要符合[文本短信模板规范](~~108253~~)或[国际/港澳台短信模板规范](~~108254~~)。""",
    )

    # 例子: 当前的短信模板应用于双11大促推广营销
    Remark: str = Field(..., title=f"""短信模板申请说明。请在申请说明中描述您的业务使用场景，长度为1~100个字符。""")

    # 例子: 155780923770
    OwnerId: Optional[int] = Field(None, title=f"""RAM用户的虚拟账号ID。""")

    Action: str = Field("AddSmsTemplate", title="系统的Action")


class ModifySmsTemplateQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    TemplateType: int = Field(..., title=f"""""")

    TemplateName: str = Field(..., title=f"""""")

    TemplateCode: str = Field(..., title=f"""""")

    TemplateContent: str = Field(..., title=f"""""")

    Remark: str = Field(..., title=f"""""")

    OwnerId: Optional[int] = Field(None, title=f"""""")

    Action: str = Field("ModifySmsTemplate", title="系统的Action")


class QuerySmsTemplateQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    TemplateCode: str = Field(..., title=f"""""")

    OwnerId: Optional[int] = Field(None, title=f"""""")

    Action: str = Field("QuerySmsTemplate", title="系统的Action")


class DeleteSmsTemplateQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    TemplateCode: str = Field(..., title=f"""""")

    OwnerId: Optional[int] = Field(None, title=f"""""")

    Action: str = Field("DeleteSmsTemplate", title="系统的Action")


class QuerySmsSignQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    SignName: str = Field(..., title=f"""""")

    OwnerId: Optional[int] = Field(None, title=f"""""")

    Action: str = Field("QuerySmsSign", title="系统的Action")


class AddShortUrlQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    OwnerId: Optional[int] = Field(None, title=f"""""")

    Action: str = Field("AddShortUrl", title="系统的Action")


class AddShortUrlBodyParams(BaseModel):
    SourceUrl: Optional[str] = Field(None, title=f"""""")

    ShortUrlName: Optional[str] = Field(None, title=f"""""")

    EffectiveDays: Optional[str] = Field(None, title=f"""""")

    ProdCode: Optional[str] = Field(None, title=f"""""")

    Action: str = Field("AddShortUrl", title="系统的Action")


class CreateShortParamQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    OwnerId: Optional[int] = Field(None, title=f"""""")

    Action: str = Field("CreateShortParam", title="系统的Action")


class CreateShortParamBodyParams(BaseModel):
    PhoneNumbers: Optional[str] = Field(None, title=f"""""")

    ProdCode: Optional[str] = Field(None, title=f"""""")

    Action: str = Field("CreateShortParam", title="系统的Action")


class DeleteShortUrlQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    OwnerId: Optional[int] = Field(None, title=f"""""")

    Action: str = Field("DeleteShortUrl", title="系统的Action")


class DeleteShortUrlBodyParams(BaseModel):
    SourceUrl: Optional[str] = Field(None, title=f"""""")

    ProdCode: Optional[str] = Field(None, title=f"""""")

    Action: str = Field("DeleteShortUrl", title="系统的Action")


class QueryShortUrlQueryParams(BaseModel):
    RegionId: Optional[str] = Field(None, title=f"""""")

    OwnerId: Optional[int] = Field(None, title=f"""""")

    Action: str = Field("QueryShortUrl", title="系统的Action")


class QueryShortUrlBodyParams(BaseModel):
    ProdCode: Optional[str] = Field(None, title=f"""""")

    ShortUrl: Optional[str] = Field(None, title=f"""""")

    Action: str = Field("QueryShortUrl", title="系统的Action")


class SmsSendDetailDTO(BaseModel):
    PhoneNum: str = Field(..., title=f"""接收短信的手机号码。""")
    SendStatus: int = Field(
        ...,
        title=f"""短信发送状态，包括：

- 1：等待回执。
- 2：发送失败。
- 3：发送成功。""",
    )
    ErrCode: str = Field(
        ...,
        title=f"""运营商短信状态码。

-  短信发送成功：DELIVRD。
-  短信发送失败：失败错误码请参考[错误码文档](~~101347~~)。""",
    )
    TemplateCode: str = Field(..., title=f"""短信模板ID。""")
    Content: str = Field(..., title=f"""短信内容。""")
    SendDate: str = Field(..., title=f"""短信发送日期和时间。""")
    ReceiveDate: str = Field(..., title=f"""短信接收日期和时间。""")
    OutId: str = Field(..., title=f"""外部流水扩展字段。""")


class QuerySendDetailsResp(BaseModel):
    RequestId: str = Field(..., title=f"""请求ID。""")
    Code: str = Field(
        ...,
        title=f"""请求状态码。
- 返回OK代表请求成功。
- 其他错误码详见[错误码列表](~~101346~~)。""",
    )
    Message: str = Field(..., title=f"""状态码的描述。""")
    TotalCount: str = Field(..., title=f"""短信发送总条数。""")

    SmsSendDetailDTOs: List[SmsSendDetailDTO] = Field(..., title="详细数据")


class SendBatchSmsResp(BaseModel):
    RequestId: str = Field(..., title=f"""请求ID。""")
    BizId: str = Field(..., title=f"""发送回执ID，可根据该ID在接口QuerySendDetails中查询具体的发送状态。""")
    Code: str = Field(
        ...,
        title=f"""请求状态码。
* 返回OK代表请求成功。
* 其他错误码详见[错误码列表](~~101346~~)。""",
    )
    Message: str = Field(..., title=f"""状态码的描述。""")


class SendSmsResp(BaseModel):
    RequestId: str = Field(..., title=f"""请求ID。""")
    BizId: str = Field(..., title=f"""发送回执ID，可根据该ID在接口QuerySendDetails中查询具体的发送状态。""")
    Code: str = Field(
        ...,
        title=f"""请求状态码。
* 返回OK代表请求成功。
* 其他错误码详见[错误码列表](~~101346~~)。""",
    )
    Message: str = Field(..., title=f"""状态码的描述。""")


class AddSmsSignResp(BaseModel):
    RequestId: str = Field(..., title=f"""请求ID。""")
    SignName: str = Field(..., title=f"""签名名称。""")
    Code: str = Field(
        ...,
        title=f"""请求状态码。
* 返回OK代表请求成功。
* 其他错误码详见[错误码列表](~~101346~~)。""",
    )
    Message: str = Field(..., title=f"""状态码的描述。""")


class DeleteSmsSignResp(BaseModel):
    RequestId: str = Field(..., title=f"""请求ID。""")
    SignName: str = Field(..., title=f"""签名名称。""")
    Code: str = Field(
        ...,
        title=f"""请求状态码。
* 返回OK代表请求成功。
* 其他错误码详见[错误码列表](~~101346~~)。""",
    )
    Message: str = Field(..., title=f"""状态码的描述。""")


class ModifySmsSignResp(BaseModel):
    RequestId: str = Field(..., title=f"""请求ID。""")
    SignName: str = Field(..., title=f"""签名名称。""")
    Code: str = Field(
        ...,
        title=f"""请求状态码。
* 返回OK代表请求成功。
* 其他错误码详见[错误码列表](~~101346~~)。""",
    )
    Message: str = Field(..., title=f"""状态码的描述。""")


class AddSmsTemplateResp(BaseModel):
    RequestId: str = Field(..., title=f"""请求ID。""")
    TemplateCode: str = Field(
        ...,
        title=f"""短信模板CODE。您可以使用模板CODE通过API接口**QuerySmsTemplate**或在控制台查看模板申请状态和结果。""",
    )
    Code: str = Field(
        ...,
        title=f"""请求状态码。
* 返回OK代表请求成功。
* 其他错误码详见[错误码列表](~~101346~~)。""",
    )
    Message: str = Field(..., title=f"""状态码的描述。""")


class ModifySmsTemplateResp(BaseModel):
    RequestId: str = Field(..., title=f"""""")
    TemplateCode: str = Field(..., title=f"""""")
    Code: str = Field(..., title=f"""""")
    Message: str = Field(..., title=f"""""")


class QuerySmsTemplateResp(BaseModel):
    RequestId: str = Field(..., title=f"""""")
    Code: str = Field(..., title=f"""""")
    Message: str = Field(..., title=f"""""")
    TemplateStatus: int = Field(..., title=f"""""")
    Reason: str = Field(..., title=f"""""")
    TemplateCode: str = Field(..., title=f"""""")
    TemplateType: int = Field(..., title=f"""""")
    TemplateName: str = Field(..., title=f"""""")
    TemplateContent: str = Field(..., title=f"""""")
    CreateDate: str = Field(..., title=f"""""")


class DeleteSmsTemplateResp(BaseModel):
    RequestId: str = Field(..., title=f"""""")
    TemplateCode: str = Field(..., title=f"""""")
    Code: str = Field(..., title=f"""""")
    Message: str = Field(..., title=f"""""")


class QuerySmsSignResp(BaseModel):
    RequestId: str = Field(..., title=f"""""")
    Code: str = Field(..., title=f"""""")
    Message: str = Field(..., title=f"""""")
    SignStatus: int = Field(..., title=f"""""")
    Reason: str = Field(..., title=f"""""")
    SignName: str = Field(..., title=f"""""")
    CreateDate: str = Field(..., title=f"""""")


class AddShortUrlRespData(BaseModel):
    SourceUrl: str = Field(..., title=f"""""")
    ExpireDate: str = Field(..., title=f"""""")
    ShortUrl: str = Field(..., title=f"""""")


class AddShortUrlResp(BaseModel):
    RequestId: str = Field(..., title=f"""""")
    Code: str = Field(..., title=f"""""")
    Message: str = Field(..., title=f"""""")

    Data: AddShortUrlRespData = Field(..., title="详细数据")


class CreateShortParamRespData(BaseModel):
    ParamDetail: str = Field(..., title=f"""""")
    PhoneNumbers: str = Field(..., title=f"""""")
    ShortParam: str = Field(..., title=f"""""")


class CreateShortParamResp(BaseModel):
    RequestId: str = Field(..., title=f"""""")
    Code: str = Field(..., title=f"""""")
    Message: str = Field(..., title=f"""""")

    Data: CreateShortParamRespData = Field(..., title="详细数据")


class DeleteShortUrlResp(BaseModel):
    RequestId: str = Field(..., title=f"""""")
    Code: str = Field(..., title=f"""""")
    Message: str = Field(..., title=f"""""")
    Data: str = Field(..., title=f"""""")


class QueryShortUrlRespData(BaseModel):
    SourceUrl: str = Field(..., title=f"""""")
    ShortUrlName: str = Field(..., title=f"""""")
    ShortUrlStatus: str = Field(..., title=f"""""")
    ShortUrl: str = Field(..., title=f"""""")
    CreateDate: str = Field(..., title=f"""""")
    ExpireDate: str = Field(..., title=f"""""")
    PageViewCount: str = Field(..., title=f"""""")
    UniqueVisitorCount: str = Field(..., title=f"""""")


class QueryShortUrlResp(BaseModel):
    RequestId: str = Field(..., title=f"""""")
    Code: str = Field(..., title=f"""""")
    Message: str = Field(..., title=f"""""")

    Data: QueryShortUrlRespData = Field(..., title="详细数据")


class AliSmsSync(AliSmsBase):
    def __init__(self, **kwargs):
        super(AliSmsSync, self).__init__(**kwargs)
        self._session = requests.Session()

    def _do_request(self, d: dict) -> Optional[dict]:
        args = self.merge_args(d, "POST")
        query = parse.urlencode(args)
        url = f"{self.endpoint}?{query}"
        resp: requests.Response = self._session.post(url)
        if resp.ok:
            return resp.json()
        return None

    def query_send_details(
        self, query: QuerySendDetailsQueryParams
    ) -> Optional[QuerySendDetailsResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return QuerySendDetailsResp(**ret)

    def send_batch_sms(
        self, query: SendBatchSmsQueryParams
    ) -> Optional[SendBatchSmsResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return SendBatchSmsResp(**ret)

    def send_sms(self, query: SendSmsQueryParams) -> Optional[SendSmsResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return SendSmsResp(**ret)

    def add_sms_sign(self, query: AddSmsSignQueryParams) -> Optional[AddSmsSignResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return AddSmsSignResp(**ret)

    def delete_sms_sign(
        self, query: DeleteSmsSignQueryParams
    ) -> Optional[DeleteSmsSignResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return DeleteSmsSignResp(**ret)

    def modify_sms_sign(
        self, query: ModifySmsSignQueryParams
    ) -> Optional[ModifySmsSignResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return ModifySmsSignResp(**ret)

    def add_sms_template(
        self, query: AddSmsTemplateQueryParams
    ) -> Optional[AddSmsTemplateResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return AddSmsTemplateResp(**ret)

    def modify_sms_template(
        self, query: ModifySmsTemplateQueryParams
    ) -> Optional[ModifySmsTemplateResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return ModifySmsTemplateResp(**ret)

    def query_sms_template(
        self, query: QuerySmsTemplateQueryParams
    ) -> Optional[QuerySmsTemplateResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return QuerySmsTemplateResp(**ret)

    def delete_sms_template(
        self, query: DeleteSmsTemplateQueryParams
    ) -> Optional[DeleteSmsTemplateResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return DeleteSmsTemplateResp(**ret)

    def query_sms_sign(
        self, query: QuerySmsSignQueryParams
    ) -> Optional[QuerySmsSignResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return QuerySmsSignResp(**ret)

    def add_short_url(
        self, query: AddShortUrlQueryParams, body: AddShortUrlBodyParams
    ) -> Optional[AddShortUrlResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return AddShortUrlResp(**ret)

    def create_short_param(
        self, query: CreateShortParamQueryParams, body: CreateShortParamBodyParams
    ) -> Optional[CreateShortParamResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return CreateShortParamResp(**ret)

    def delete_short_url(
        self, query: DeleteShortUrlQueryParams, body: DeleteShortUrlBodyParams
    ) -> Optional[DeleteShortUrlResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return DeleteShortUrlResp(**ret)

    def query_short_url(
        self, query: QueryShortUrlQueryParams, body: QueryShortUrlBodyParams
    ) -> Optional[QueryShortUrlResp]:
        ret = self._do_request(query.dict())
        if ret is None:
            return None
        return QueryShortUrlResp(**ret)


class AliSmsAsync(AliSmsBase):
    def __init__(self, **kwargs):
        super(AliSmsAsync, self).__init__(**kwargs)
        self._session = ClientSession()

    async def _do_request(self, d: dict) -> Optional[dict]:
        args = self.merge_args(d, "POST")
        query = parse.urlencode(args)
        url = f"{self.endpoint}?{query}"
        resp: ClientResponse = await self._session.post(url)
        if 200 <= resp.status < 300:
            return await resp.json()
        return None

    async def query_send_details(
        self, query: QuerySendDetailsQueryParams
    ) -> Optional[QuerySendDetailsResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return QuerySendDetailsResp(**ret)

    async def send_batch_sms(
        self, query: SendBatchSmsQueryParams
    ) -> Optional[SendBatchSmsResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return SendBatchSmsResp(**ret)

    async def send_sms(self, query: SendSmsQueryParams) -> Optional[SendSmsResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return SendSmsResp(**ret)

    async def add_sms_sign(
        self, query: AddSmsSignQueryParams
    ) -> Optional[AddSmsSignResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return AddSmsSignResp(**ret)

    async def delete_sms_sign(
        self, query: DeleteSmsSignQueryParams
    ) -> Optional[DeleteSmsSignResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return DeleteSmsSignResp(**ret)

    async def modify_sms_sign(
        self, query: ModifySmsSignQueryParams
    ) -> Optional[ModifySmsSignResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return ModifySmsSignResp(**ret)

    async def add_sms_template(
        self, query: AddSmsTemplateQueryParams
    ) -> Optional[AddSmsTemplateResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return AddSmsTemplateResp(**ret)

    async def modify_sms_template(
        self, query: ModifySmsTemplateQueryParams
    ) -> Optional[ModifySmsTemplateResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return ModifySmsTemplateResp(**ret)

    async def query_sms_template(
        self, query: QuerySmsTemplateQueryParams
    ) -> Optional[QuerySmsTemplateResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return QuerySmsTemplateResp(**ret)

    async def delete_sms_template(
        self, query: DeleteSmsTemplateQueryParams
    ) -> Optional[DeleteSmsTemplateResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return DeleteSmsTemplateResp(**ret)

    async def query_sms_sign(
        self, query: QuerySmsSignQueryParams
    ) -> Optional[QuerySmsSignResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return QuerySmsSignResp(**ret)

    async def add_short_url(
        self, query: AddShortUrlQueryParams, body: AddShortUrlBodyParams
    ) -> Optional[AddShortUrlResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return AddShortUrlResp(**ret)

    async def create_short_param(
        self, query: CreateShortParamQueryParams, body: CreateShortParamBodyParams
    ) -> Optional[CreateShortParamResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return CreateShortParamResp(**ret)

    async def delete_short_url(
        self, query: DeleteShortUrlQueryParams, body: DeleteShortUrlBodyParams
    ) -> Optional[DeleteShortUrlResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return DeleteShortUrlResp(**ret)

    async def query_short_url(
        self, query: QueryShortUrlQueryParams, body: QueryShortUrlBodyParams
    ) -> Optional[QueryShortUrlResp]:
        ret = await self._do_request(query.dict())
        if ret is None:
            return None
        return QueryShortUrlResp(**ret)
