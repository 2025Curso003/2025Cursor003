/**
 * 检查所有优惠券的所有批次详情的状态是否与指定状态匹配
 * @param couponDataList 优惠券数据列表
 * @param state 要检查的状态值
 * @throws IllegalArgumentException 当参数为空时抛出
 * @throws BusinessException 当优惠券状态不匹配时抛出
 */
private void checkAllCouponsState(List<ReceiveGiftData.CouponData> couponDataList, Integer state) {
    // 参数校验
    if (couponDataList == null || couponDataList.isEmpty()) {
        throw new IllegalArgumentException("优惠券列表不能为空");
    }
    if (state == null || !CouponStateEnum.isValidCode(state)) {
        throw new IllegalArgumentException("无效的优惠券状态码: " + state);
    }

    // 期望的状态描述
    String expectedStateDesc = CouponStateEnum.getDescriptionByCode(state);

    for (ReceiveGiftData.CouponData couponData : couponDataList) {
        // 检查batchFromRecordIdDetailCOList是否存在且不为空
        if (couponData.getBatchFromRecordIdDetailCOList() == null
                || couponData.getBatchFromRecordIdDetailCOList().isEmpty()) {
            throw new BusinessException("优惠券详情列表不能为空");
        }

        // 检查每个批次详情的状态
        for (BatchFromRecordIdDetail detail : couponData.getBatchFromRecordIdDetailCOList()) {
            if (detail == null) {
                throw new BusinessException("优惠券批次详情不能为空");
            }
            
            if (!state.equals(detail.getState())) {
                String actualStateDesc = CouponStateEnum.getDescriptionByCode(detail.getState());
                throw new BusinessException(String.format(
                    "优惠券状态不匹配，期望状态：%s，实际状态：%s，优惠券ID：%s",
                    expectedStateDesc,
                    actualStateDesc,
                    detail.getCouponId()
                ));
            }
        }
    }
} 