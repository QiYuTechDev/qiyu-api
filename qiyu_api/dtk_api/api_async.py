from .gen import *

__all__ = ["DtkAsyncApi"]


class DtkAsyncApi(object):
    """"""

    def __init__(self, app_key: str, app_secret: str):
        self._inner = DtkAsync(app_key=app_key, app_secret=app_secret)

    @staticmethod
    def _generic_get_data(d: Optional[dict]) -> Optional[dict]:
        if isinstance(d, dict) and d["code"] == 0:
            return d["data"]
        return None

    async def goods_price_trend(
        self, args: GoodsPriceTrendArgs
    ) -> Optional[GoodsPriceTrendResp]:
        """
        doc: https://www.dataoke.com/pmc/api-d.html?id=36
        """
        ret = await self._inner.goods_price_trend(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return GoodsPriceTrendResp(**data)

    async def goods_liveMaterial_goods_list(
        self, args: GoodsLivematerialGoodsListArgs
    ) -> Optional[dict]:
        return await self._inner.goods_liveMaterial_goods_list(args)

    async def goods_explosive_goods_list(
        self, args: GoodsExplosiveGoodsListArgs
    ) -> Optional[List[GoodsExplosiveGoodsListResp]]:
        ret = await self._inner.goods_explosive_goods_list(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return list(map(lambda x: GoodsExplosiveGoodsListResp(**x), data["list"]))

    async def tb_service_parse_content(
        self, args: TbServiceParseContentArgs
    ) -> Optional[dict]:
        return await self._inner.tb_service_parse_content(args)

    async def goods_exclusive_goods_list(
        self, args: GoodsExclusiveGoodsListArgs
    ) -> Optional[List[GoodsExclusiveGoodsListResp]]:
        ret = await self._inner.goods_exclusive_goods_list(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return list(map(lambda x: GoodsExclusiveGoodsListResp(**x), data["list"]))

    async def tb_service_activity_link(
        self, args: TbServiceActivityLinkArgs
    ) -> Optional[TbServiceGetPrivilegeLinkResp]:
        ret = await self._inner.tb_service_activity_link(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return TbServiceGetPrivilegeLinkResp(**data)

    async def tb_service_twd_to_twd(
        self, args: TbServiceTwdToTwdArgs
    ) -> Optional[dict]:
        return await self._inner.tb_service_twd_to_twd(args)

    async def goods_first_order_gift_money(
        self, args: GoodsFirstOrderGiftMoneyArgs
    ) -> Optional[dict]:
        return await self._inner.goods_first_order_gift_money(args)

    async def tb_service_creat_taokouling(
        self, args: TbServiceCreatTaokoulingArgs
    ) -> Optional[TbServiceCreatTaokoulingResp]:
        ret = await self._inner.tb_service_creat_taokouling(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return TbServiceCreatTaokoulingResp(**data)

    async def tb_service_get_order_details(
        self, args: TbServiceGetOrderDetailsArgs
    ) -> Optional[dict]:
        return await self._inner.tb_service_get_order_details(args)

    async def tb_service_parse_taokouling(
        self, args: TbServiceParseTaokoulingArgs
    ) -> Optional[TbServiceParseTaokoulingResp]:
        ret = await self._inner.tb_service_parse_taokouling(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return TbServiceParseTaokoulingResp(**data)

    async def tb_service_get_privilege_link(
        self, args: TbServiceGetPrivilegeLinkArgs
    ) -> Optional[TbServiceGetPrivilegeLinkResp]:
        ret = await self._inner.tb_service_get_privilege_link(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return TbServiceGetPrivilegeLinkResp(**data)

    async def goods_nine_op_goods_list(
        self, args: GoodsNineOpGoodsListArgs
    ) -> Optional[GoodsNineOpGoodsListResp]:
        ret = await self._inner.goods_nine_op_goods_list(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return GoodsNineOpGoodsListResp(**data)

    async def category_ddq_goods_list(
        self, args: CategoryDdqGoodsListArgs
    ) -> Optional[CategoryDdqGoodsListResp]:
        ret = await self._inner.category_ddq_goods_list(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return CategoryDdqGoodsListResp(**data)

    async def goods_get_ranking_list(
        self, args: GoodsGetRankingListArgs
    ) -> Optional[List[GoodsGetRankingListResp]]:
        ret = await self._inner.goods_get_ranking_list(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return list(map(lambda x: GoodsGetRankingListResp(**x), data))

    async def goods_friends_circle_list(
        self, args: GoodsFriendsCircleListArgs
    ) -> Optional[dict]:
        return await self._inner.goods_friends_circle_list(args)

    async def goods_topic_catalogue(self) -> Optional[List[GoodsTopicCatalogueResp]]:
        ret = await self._inner.goods_topic_catalogue()
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return list(map(lambda x: GoodsTopicCatalogueResp(**x), data))

    async def goods_topic_goods_list(
        self, args: GoodsTopicGoodsListArgs
    ) -> Optional[dict]:
        return await self._inner.goods_topic_goods_list(args)

    async def category_get_tb_topic_list(
        self, args: CategoryGetTbTopicListArgs
    ) -> Optional[dict]:
        return await self._inner.category_get_tb_topic_list(args)

    async def tb_service_get_brand_list(
        self, args: TbServiceGetBrandListArgs
    ) -> Optional[List[TbServiceGetBrandListResp]]:
        ret = await self._inner.tb_service_get_brand_list(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return list(map(lambda x: TbServiceGetBrandListResp(**x), data))

    async def goods_search_suggestion(
        self, args: GoodsSearchSuggestionArgs
    ) -> Optional[List[GoodsSearchSuggestionResp]]:
        ret = await self._inner.goods_search_suggestion(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return list(map(lambda x: GoodsSearchSuggestionResp(**x), data))

    async def goods_list_super_goods(
        self, args: GoodsListSuperGoodsArgs
    ) -> Optional[List[GoodsListSuperGoodsResp]]:
        ret = await self._inner.goods_list_super_goods(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return list(map(lambda x: GoodsListSuperGoodsResp(**x), data["list"]))

    async def goods_list_similer_goods_by_open(
        self, args: GoodsListSimilerGoodsByOpenArgs
    ) -> Optional[List[GoodsListSimilerGoodsByOpenResp]]:
        ret = await self._inner.goods_list_similer_goods_by_open(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return list(map(lambda x: GoodsListSimilerGoodsByOpenResp(**x), data))

    async def goods_get_goods_list(
        self, args: GoodsGetGoodsListArgs
    ) -> Optional[List[GoodsGetGoodsListResp]]:
        ret = await self._inner.goods_get_goods_list(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return list(map(lambda x: GoodsGetGoodsListResp(**x), data["list"]))

    async def goods_get_goods_details(
        self, args: GoodsGetGoodsDetailsArgs
    ) -> Optional[GoodsGetGoodsDetailsResp]:
        ret = await self._inner.goods_get_goods_details(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return GoodsGetGoodsDetailsResp(**data)

    async def goods_get_dtk_search_goods(
        self, args: GoodsGetDtkSearchGoodsArgs
    ) -> Optional[GoodsGetDtkSearchGoodsResp]:
        ret = await self._inner.goods_get_dtk_search_goods(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return GoodsGetDtkSearchGoodsResp(**data)

    async def goods_pull_goods_by_time(
        self, args: GoodsPullGoodsByTimeArgs
    ) -> Optional[dict]:
        return await self._inner.goods_pull_goods_by_time(args)

    async def category_get_top100(self) -> Optional[CategoryGetTop100Resp]:
        ret = await self._inner.category_get_top100()
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return CategoryGetTop100Resp(**data)

    async def goods_get_stale_goods_by_time(
        self, args: GoodsGetStaleGoodsByTimeArgs
    ) -> Optional[dict]:
        return await self._inner.goods_get_stale_goods_by_time(args)

    async def goods_get_newest_goods(
        self, args: GoodsGetNewestGoodsArgs
    ) -> Optional[dict]:
        return await self._inner.goods_get_newest_goods(args)

    async def category_get_super_category(
        self,
    ) -> Optional[List[CategoryGetSuperCategoryResp]]:
        ret = await self._inner.category_get_super_category()
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return list(map(lambda x: CategoryGetSuperCategoryResp(**x), data))

    async def tb_service_get_tb_service(
        self, args: TbServiceGetTbServiceArgs
    ) -> Optional[List[TbServiceGetTbServiceResp]]:
        ret = await self._inner.tb_service_get_tb_service(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return list(map(lambda x: TbServiceGetTbServiceResp(**x), data))

    async def goods_get_collection_list(
        self, args: GoodsGetCollectionListArgs
    ) -> Optional[dict]:
        return await self._inner.goods_get_collection_list(args)

    async def goods_get_owner_goods(
        self, args: GoodsGetOwnerGoodsArgs
    ) -> Optional[dict]:
        return await self._inner.goods_get_owner_goods(args)

    async def goods_activity_goods_list(
        self, args: GoodsActivityGoodsListArgs
    ) -> Optional[dict]:
        return await self._inner.goods_activity_goods_list(args)

    async def goods_activity_catalogue(
        self,
    ) -> Optional[List[GoodsActivityCatalogueResp]]:
        ret = await self._inner.goods_activity_catalogue()
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return list(map(lambda x: GoodsActivityCatalogueResp(**x), data))

    async def delanys_brand_get_goods_list(
        self, args: DelanysBrandGetGoodsListArgs
    ) -> Optional[List[DelanysBrandGetGoodsListResp]]:

        ret = await self._inner.delanys_brand_get_goods_list(args)
        data = self._generic_get_data(ret)
        if data is None:
            return None
        return list(map(lambda x: DelanysBrandGetGoodsListResp(**x), data["list"]))
