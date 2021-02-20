from pydantic import Field

__all__ = ["page_field", "page_size_field", "cid_field", "sort_fields"]

token = Field(..., title="认证 TOKEN", description="用户用来认证的 token, 登陆的时候获取到的")
token_optional = Field(None, title="认证 TOKEN", description="用户用来认证的 token, 登陆的时候获取到的")

page_field = Field(1, gt=0, title="分页", description="第几页面")
page_size_field = Field(20, ge=10, le=50, title="每页数据条数", description="可自定义 10~50 之间")
cid_field = Field(
    None,
    title="一级商品分类",
    description="""一级商品分类
值为空：全部商品
1：女装
2：母婴
3：美妆
4：居家日用
5：鞋品
6：美食
7：文娱车品
8：数码家电
9：男装
10：内衣
11：箱包
12：配饰
13：户外运动
14：家装家纺
""",
)
sort_fields = Field(
    "new",
    title="商品排序方式",
    description="""
new：按照综合排序\n
total_sale_num_asc：按照总销量从小到大排序\n
total_sale_num_desc：按照总销量从大到小排序\n
sale_num_asc：按照月销量从小到大排序\n
sale_num_desc：按照月销量从大到小排序\n
commission_rate_asc：按照佣金比例从小到大排序\n
commission_rate_desc：按照佣金比例从大到小排序\n
price_asc：按照价格从小到大排序\n
price_desc：按照价格从大到小排序\n
coupon_info_money_asc：按照优惠券金额从小到大排序\n
coupon_info_money_desc：按照优惠券金额从大到小排序\n
shop_level_asc：按照店铺等级从低到高排序\n
shop_level_desc：按照店铺等级从高到低排序\n
tkfee_asc：按照返佣金额从低到高排序\n
tkfee_desc：按照返佣金额从高到低排序\n
code：按照code值从大到小排序\n
date_time：按照更新时间排序\n
random：按照随机排序\n
""",
)

code_field = Field(..., title="折淘客编号")
type_one_id_field = Field(..., title="分类 id, 参见: cid")
tao_id_field = Field(
    ..., title="淘宝的商品 id", description="都是同一个意思: item_id/num_iid/tao_id"
)
title_field = Field(..., title="商品的标题")
jianjie_field = Field(..., title="商品的简介")
pict_url_field = Field(..., title="商品的主图")
user_type_field = Field(..., title="卖家类型", description="0表示集市，1表示商城")
seller_id_field = Field(..., title="商家的 id")
shop_dsr_field = Field(..., title="店铺 dsr 评分")
volume_field = Field(..., title="30天销量")
size_field = Field(..., title="折扣价")
quanhou_jiage_field = Field(..., title="券后价格")
date_time_yongjin_field = Field(
    ..., title="数据更新时间", description="例如: 2020/06/25 20:35:46"
)
tkrate3_field = Field(..., title="佣金比例", description="例如: 25.00 表示 25.0%")
yongjin_type_field = Field(..., title="佣金类型", description="例如: MKT")
coupon_id_field = Field(..., title="优惠券ID", description="")
coupon_start_time_field = Field(..., title="优惠券开始时间", description="例如: 2020-10-10")
coupon_end_time_field = Field(..., title="优惠券结束时间", description="例如: 2020-10-10")
coupon_info_money_field = Field(..., title="优惠券金额", description="例如: 70.00 单位: 元")
coupon_total_count_field = Field(..., title="优惠券总量")
coupon_remain_count_field = Field(..., title="优惠券剩余数量")
coupon_info_field = Field(..., title="优惠券信息")
juhuasuan_field = Field(..., title="是否为 聚划算", description="0 否 1 是, 注意: 是字符串")
taoqianggou_field = Field(..., title="是否为 淘抢购", description="0 否 1 是, 注意: 是字符串")
haitao_field = Field(..., title="是否为 海淘", description="0 否 1 是, 注意: 是字符串")
jiyoujia_field = Field(..., title="是否极有家", description="0 否 1 是, 注意: 是字符串")
jinpaimaijia_field = Field(..., title="是否为 金牌卖家", description="0 否 1 是, 注意: 是字符串")
pinpai_field = Field(..., title="是否为 品牌", description="0 否 1 是, 注意: 是字符串")
pinpai_name_field = Field(..., title="品牌名称")
yunfeixian_feild = Field(..., title="是否有运费险", description="1有")
nick_field = Field(..., title="店铺名称")
small_images_field = Field(
    ..., title="商品组图/商品小图列表", description="商品组图, 为多个 url, 使用 | 分割"
)
white_image_field = Field(..., title="商品白底图")
tao_title_field = Field(..., title="商品长标题")
provcity_field = Field(..., title="省份 城市")
shop_title_field = Field(..., title="商家名称")
zhibo_url_field = Field(..., title="直播地址")
sellCount_field = Field(..., title="销售数量")
commentCount_field = Field(..., title="评论数量")
favcount_field = Field(..., title="喜欢数量")
score1_field = Field(..., title="宝贝描述分")
score2_field = Field(..., title="卖家服务分")
score3_field = Field(..., title="物流服务分")
creditLevel_field = Field(
    ...,
    title="店铺等级",
    description="""1-20:
一星 二星 三星 四星 五星
一钻 二钻 三钻 四钻 五钻
一皇冠 二皇冠 三皇冠 四皇冠 五皇冠
一金冠 二金冠 三金冠 四金冠 五金冠
""",
)
shopIcon_field = Field(..., title="商家图标 URL")
pcDescContent_field = Field(..., title="内容 url", description="多个 url 地址 使用 | 分隔开")
item_url_field = Field(..., title="商品地址")
category_id_field = Field(..., title="分类 id")
category_name_field = Field(..., title="分类名称")
level_one_category_id_field = Field(..., title="???")
level_one_category_name_field = Field(..., title="???")
tkfee3_field = Field(..., title="???")

volume_shishi_field = Field(..., title="两小时销量")
volume_quantian_field = Field(..., title="全天销量")
tk_sale_count_field = Field(..., title="人气值")
biaoqian_field = Field(..., title="店铺活动", description="满300元,省30元")
tag_field = Field(
    ...,
    title="朋友圈文案",
    description="例如: 赶紧拯救你厨房的油腻吧😂植护🌿加厚厨房抽纸高密度纤维纸张，吸油💧很不错5包装|￥14.8元💰✔厨房小帮手，用处多多",
)
presale_discount_fee_text_field = Field(
    None, title="预售商品-商品优惠信息", description="例如: 付定金立减20元"
)
presale_tail_end_time_field = Field(None, title="预售商品-付定金结束时间（毫秒）")
presale_tail_start_time_field = Field(None, title="预售商品-付尾款开始时间（毫秒）")
presale_end_time_field = Field(None, title="预售结束时间")
presale_start_time_field = Field(None, title="预售开始时间")
presale_deposit_field = Field(None, title="预售 ???")
yunfeixian_field = Field(..., title="???")

cat_leaf_name_field = Field(..., title="叶子类目名称", description="例如: 情趣内衣")
cat_name_field = Field(..., title="一级类目名称", description="例如: 女装")
ju_online_end_time_field = Field(..., title="聚划算信息-聚淘开始时间（毫秒）")
ju_online_start_time_field = Field(..., title="聚划算信息-聚淘结束时间（毫秒）")
ju_pre_show_end_time_field = Field(..., title="聚划算信息-商品预热结束时间（毫秒）")
ju_pre_show_start_time_field = Field(..., title="聚划算信息-商品预热开始时间（毫秒）")
material_lib_type_field = Field(
    ...,
    title="商品库类型",
    description="支持多库类型输出，以英文逗号分隔“,”分隔\n1:营销商品主推库\n2. 内容商品库，如果值为空则不属于1，2这两种商品类型",
)
num_iid_field = tao_id_field
reserve_price_field = Field(..., title="商品一口价格")
tmall_play_activity_end_time_field = Field(..., title="天猫限时抢可售 -结束时间（毫秒）")
tmall_play_activity_start_time_field = Field(..., title="天猫限时抢可售 -开始时间（毫秒）")
zk_final_price_field = Field(..., title="折扣价（元）若属于预售商品，付定金时间内，折扣价=预售价")
kuadian_promotion_info_field = Field(
    ..., title="跨店满减信息", description='例如: ["每100减20","每200减50"]'
)

date_time_field = Field(..., title="数据添加时间", description="")
min_commission_rate_field = Field(..., title="", description="")

order_type = Field(..., title="订单类型", description="")

taobao_url_field = Field(..., title="商品URL")
coupon_click_url_field = Field(..., title="二合一推广链接，已经自动拼接S券")
shorturl_field = Field(..., title="淘宝短链接")
tkl_field = Field(..., title="淘口令")
