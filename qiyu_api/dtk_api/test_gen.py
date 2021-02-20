"""
代码生成模块测试
"""

import os
import sys

from .gen import *
from .test_shared import get_id, get_dtk_sync, get_goods_id, get_uland_url


def convert_name_to_py_class_name(name: str) -> str:
    parts = name.split("_")
    out = "".join(map(lambda x: x.capitalize(), parts))
    return f"{out}Resp"


def gen_with_class_name(class_name: str, data: dict) -> str:
    fields = []
    sub_codes = []
    for name, value in data.items():
        typ = type(value)
        if typ is str:
            fields.append(f"""    {name}: Optional[str] = Field(None)""")
        elif typ is int:
            fields.append(f"""    {name}: Optional[int] = Field(None)""")
        elif typ is float:
            fields.append(f"""    {name}: Optional[float] = Field(None)""")
        elif typ is dict:
            sub_name, sub_code = gen_sub_field(class_name, name, value)
            fields.append(f"""    {name}: Optional[{sub_name}] = Field(None)""")
            sub_codes.append(sub_code)
        elif typ is list:
            if len(value) >= 1:
                if type(value[0]) == dict:
                    sub_name, sub_code = gen_sub_field(class_name, name, value[0])
                    fields.append(
                        f"""    {name}: Optional[List[{sub_name}]] = Field(None)"""
                    )
                    sub_codes.append(sub_code)
                elif type(value[0]) == str:
                    fields.append(f"""    {name}: Optional[List[str]] = Field(None)""")
                elif type(value[0]) == int:
                    fields.append(f"""    {name}: Optional[List[int]] = Field(None)""")
                else:
                    print(f"{type(value[0])} is not handled")
                    sys.exit(3)
            else:
                fields.append(f"""    {name}: Optional[list] = Field(None)""")
        else:
            print(f"未知的类型: {typ=}")
            sys.exit(1)
    field_code = "\n".join(fields)
    sub_field_code = "\n".join(sub_codes)

    return f"""
{sub_field_code}
class {class_name}(BaseModel):
{field_code}
"""


# return value:
# 1st is sub class name
# 2nd is code
def gen_sub_field(class_name: str, field_name: str, data: dict) -> (str, str):
    sub_name = f"{class_name}{field_name.capitalize()}"

    class_dt = gen_with_class_name(sub_name, data)

    return sub_name, class_dt


def gen_one_data(name: str, data: dict) -> str:
    class_name = convert_name_to_py_class_name(name)

    fields = []
    sub_codes = []
    for name, value in data.items():
        typ = type(value)
        if typ is str:
            fields.append(f"""    {name}: Optional[str] = Field(None)""")
        elif typ is int:
            fields.append(f"""    {name}: Optional[Union[int, float]] = Field(None)""")
        elif typ is float:
            fields.append(f"""    {name}: Optional[float] = Field(None)""")
        elif typ is dict:
            sub_name, sub_code = gen_sub_field(class_name, name, value)
            fields.append(f"""    {name}: Optional[{sub_name}] = Field(None)""")
            sub_codes.append(sub_code)
        elif typ is list:
            if len(value) >= 1:
                if type(value[0]) == dict:
                    sub_name, sub_code = gen_sub_field(class_name, name, value[0])
                    fields.append(
                        f"""    {name}: Optional[List[{sub_name}]] = Field(None)"""
                    )
                    sub_codes.append(sub_code)
                elif type(value[0]) == str:
                    fields.append(f"""    {name}: Optional[List[str]] = Field(None)""")
                elif type(value[0]) == int:
                    fields.append(f"""    {name}: Optional[List[int]] = Field(None)""")
                else:
                    print(f"{type(value[0])} is not handled")
                    sys.exit(3)
            else:
                fields.append(f"""    {name}: Optional[list] = Field(None)""")
        else:
            sys.exit(1)

    field_code = "\n".join(fields)
    sub_field_code = "\n".join(sub_codes)

    return f"""
{sub_field_code}
class {class_name}(BaseModel):
{field_code}
"""


def write_to_file(code: str):
    out_file = os.path.join(os.path.dirname(__file__), "dt_resp_v2.py")
    with open(out_file, "a") as fp:
        fp.write(code)


def test_gen_category_get_super_category():
    dtk = get_dtk_sync()
    ret = dtk.category_get_super_category()
    assert ret["code"] == 0
    o = gen_one_data("category_get_super_category", ret["data"][0])
    write_to_file(o)


def test_goods_price_trend():
    dtk = get_dtk_sync()
    args = GoodsPriceTrendArgs(id=get_id())
    ret = dtk.goods_price_trend(args)
    print(ret)
    assert ret["code"] == 0
    o = gen_one_data("goods_price_trend", ret["data"])
    write_to_file(o)


def test_goods_dtk_search():
    dtk = get_dtk_sync()
    args = GoodsGetDtkSearchGoodsArgs(keyWords="手机", pageId=str(3), pageSize=str(10))
    ret = dtk.goods_get_dtk_search_goods(args)
    assert ret["code"] == 0
    o = gen_one_data("goods_get_dtk_search_goods", ret["data"])
    write_to_file(o)


def test_tb_service_get_privilege_link():
    dtk = get_dtk_sync()
    args = TbServiceGetPrivilegeLinkArgs(goodsId=get_goods_id())
    ret = dtk.tb_service_get_privilege_link(args)
    assert ret["code"] == 0
    o = gen_one_data("tb_service_get_privilege_link", ret["data"])
    write_to_file(o)


def test_goods_get_ranking_list():
    dtk = get_dtk_sync()
    args = GoodsGetRankingListArgs(rankType=str(1))
    ret = dtk.goods_get_ranking_list(args)
    assert ret["code"] == 0
    o = gen_one_data("goods_get_ranking_list", ret["data"][0])
    write_to_file(o)


def test_goods_get_goods_details():
    dtk = get_dtk_sync()
    args = GoodsGetGoodsDetailsArgs(id=get_id())
    ret = dtk.goods_get_goods_details(args)
    assert ret["code"] == 0
    o = gen_one_data("goods_get_goods_details", ret["data"])
    write_to_file(o)


def test_tb_service_get_brand_list():
    dtk = get_dtk_sync()
    args = TbServiceGetBrandListArgs(pageId=str(1), pageSize=str(10))
    ret = dtk.tb_service_get_brand_list(args)
    assert ret["code"] == 0
    o = gen_one_data("tb_service_get_brand_list", ret["data"][0])
    write_to_file(o)


def test_goods_nine_op_goods_list():
    dtk = get_dtk_sync()
    args = GoodsNineOpGoodsListArgs(pageId=str(1), pageSize=str(10), nineCid=str(1))
    ret = dtk.goods_nine_op_goods_list(args)
    assert ret["code"] == 0
    o = gen_one_data("goods_nine_op_goods_list", ret["data"])
    write_to_file(o)


def test_tb_service_get_tb_service():
    dtk = get_dtk_sync()
    args = TbServiceGetTbServiceArgs(pageNo=str(1), pageSize=str(10), keyWords="苹果")
    ret = dtk.tb_service_get_tb_service(args)
    assert ret["code"] == 0
    o = gen_one_data("tb_service_get_tb_service", ret["data"][0])
    write_to_file(o)


def test_category_get_top100():
    dtk = get_dtk_sync()
    ret = dtk.category_get_top100()
    print(ret["data"])
    assert ret["code"] == 0
    o = gen_one_data("category_get_top100", ret["data"])
    write_to_file(o)


def test_goods_get_goods_list():
    dtk = get_dtk_sync()
    args = GoodsGetGoodsListArgs(pageId=str(1), pageSize=str(10))
    ret = dtk.goods_get_goods_list(args)
    print(ret["data"]["list"][0])
    assert ret["code"] == 0
    o = gen_one_data("goods_get_goods_list", ret["data"]["list"][0])
    write_to_file(o)


def test_goods_list_super_goods():
    dtk = get_dtk_sync()
    args = GoodsListSuperGoodsArgs(
        pageId=str(1), pageSize=str(10), keyWords="iOS", type=str(0)
    )
    ret = dtk.goods_list_super_goods(args)
    print(ret)
    assert ret["code"] == 0
    o = gen_one_data("goods_list_super_goods", ret["data"]["list"][0])
    write_to_file(o)


def test_goods_list_similer_goods_by_open():
    dtk = get_dtk_sync()
    args = GoodsListSimilerGoodsByOpenArgs(id=str(get_id()))
    ret = dtk.goods_list_similer_goods_by_open(args)
    print(ret)
    assert ret["code"] == 0
    o = gen_one_data("goods_list_similer_goods_by_open", ret["data"][0])
    write_to_file(o)


def test_goods_search_suggestion():
    dtk = get_dtk_sync()
    args = GoodsSearchSuggestionArgs(keyWords="手机", type=str(1))
    ret = dtk.goods_search_suggestion(args)
    print(ret)
    assert ret["code"] == 0
    o = gen_one_data("goods_search_suggestion", ret["data"][0])
    write_to_file(o)


def test_goods_activity_catalogue():
    dtk = get_dtk_sync()
    ret = dtk.goods_activity_catalogue()
    print(ret)
    assert ret["code"] == 0
    o = gen_one_data("goods_activity_catalogue", ret["data"][0])
    write_to_file(o)


def test_goods_activity_goods_list():
    dtk = get_dtk_sync()
    # todo impl dtk.goods_activity_goods_list()


def test_goods_topic_catalogue():
    dtk = get_dtk_sync()
    ret = dtk.goods_topic_catalogue()
    print(ret)
    assert ret["code"] == 0
    o = gen_one_data("goods_topic_catalogue", ret["data"][0])
    write_to_file(o)


def test_goods_topic_goods_list():
    dtk = get_dtk_sync()
    # args = GoodsTopicGoodsListArgs()
    # ret = dtk.goods_topic_goods_list()


def test_category_ddq_goods_list():
    dtk = get_dtk_sync()
    args = CategoryDdqGoodsListArgs()
    ret = dtk.category_ddq_goods_list(args)
    print(ret)
    assert ret["code"] == 0
    o = gen_one_data("category_ddq_goods_list", ret["data"])
    write_to_file(o)


def test_tb_service_parse_taokouling():
    dtk = get_dtk_sync()
    args = TbServiceParseTaokoulingArgs(content="1￥uFkCciFmKQH￥/")
    ret = dtk.tb_service_parse_taokouling(args)
    print(ret)
    assert ret["code"] == 0
    o = gen_one_data("tb_service_parse_taokouling", ret["data"])
    write_to_file(o)


def test_tb_service_creat_taokouling():
    dtk = get_dtk_sync()
    args = TbServiceCreatTaokoulingArgs(text="hello", url=get_uland_url())
    ret = dtk.tb_service_creat_taokouling(args)
    print(ret)
    assert ret["code"] == 0
    o = gen_one_data("tb_service_creat_taokouling", ret["data"])
    write_to_file(o)


def test_goods_exclusive_goods_list():
    dtk = get_dtk_sync()
    args = GoodsExclusiveGoodsListArgs(pageId=str(1), pageSize=str(10))
    ret = dtk.goods_exclusive_goods_list(args)
    print(ret)
    assert ret["code"] == 0
    o = gen_one_data("goods_exclusive_goods_list", ret["data"]["list"][0])
    write_to_file(o)


def test_goods_explosive_goods_list():
    dtk = get_dtk_sync()
    args = GoodsExplosiveGoodsListArgs(pageId=str(1), pageSize=str(10))
    ret = dtk.goods_explosive_goods_list(args)
    assert ret["code"] == 0
    o = gen_one_data("goods_explosive_goods_list", ret["data"]["list"][0])
    write_to_file(o)


def test_delanys_brand_get_goods_list():
    dtk = get_dtk_sync()
    args = DelanysBrandGetGoodsListArgs(
        brandId="30844", pageId=str(1), pageSize=str(10)
    )
    ret = dtk.delanys_brand_get_goods_list(args)
    o = gen_one_data("delanys_brand_get_goods_list", ret["data"]["list"][0])
    write_to_file(o)


def test_slot_code():
    slot = f"""
CategoryGetTbTopicListResp = Any
GoodsActivityGoodsListResp = Any
GoodsFirstOrderGiftMoneyResp = Any
GoodsFriendsCircleListResp = Any
GoodsGetCollectionListResp = Any
GoodsGetNewestGoodsResp = Any
GoodsGetOwnerGoodsResp = Any
GoodsGetStaleGoodsByTimeResp = Any
GoodsLivematerialGoodsListResp = Any
GoodsPullGoodsByTimeResp = Any
GoodsTopicCatalogue = Any
GoodsTopicGoodsListResp = Any
TbServiceActivityLinkResp = Any
TbServiceGetOrderDetailsResp = Any
TbServiceParseContentResp = Any
TbServiceTwdToTwdResp = Any
"""
    write_to_file(slot)
