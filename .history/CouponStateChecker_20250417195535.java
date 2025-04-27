import java.util.List;

/**
 * 优惠券状态检查器
 */
public class CouponStateChecker {
    
    /**
     * 检查所有优惠券的所有批次详情的状态是否与指定状态匹配
     * @param couponDataList 优惠券数据列表
     * @param state 要检查的状态值
     * @throws IllegalArgumentException 当参数为空时抛出
     * @throws BusinessException 当优惠券状态不匹配时抛出
     */
    public void checkAllCouponsState(List<ReceiveGiftData.CouponData> couponDataList, Integer state) {
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
}

/**
 * 业务异常类
 */
class BusinessException extends RuntimeException {
    public BusinessException(String message) {
        super(message);
    }
}

/**
 * 优惠券数据类
 */
class ReceiveGiftData {
    public static class CouponData {
        private List<BatchFromRecordIdDetail> batchFromRecordIdDetailCOList;
        private String couponName;
        private String fromRecordId;
        private Integer giftType;
        private String receiveTime;

        public List<BatchFromRecordIdDetail> getBatchFromRecordIdDetailCOList() {
            return batchFromRecordIdDetailCOList;
        }

        public void setBatchFromRecordIdDetailCOList(List<BatchFromRecordIdDetail> batchFromRecordIdDetailCOList) {
            this.batchFromRecordIdDetailCOList = batchFromRecordIdDetailCOList;
        }
    }
}

/**
 * 优惠券批次详情类
 */
class BatchFromRecordIdDetail {
    private Long couponId;
    private Long couponTemplateId;
    private String couponTemplateName;
    private Integer state;
    private String createTime;
    private String effectTimeEnd;
    private String effectTimeStart;

    public Long getCouponId() {
        return couponId;
    }

    public void setCouponId(Long couponId) {
        this.couponId = couponId;
    }

    public Integer getState() {
        return state;
    }

    public void setState(Integer state) {
        this.state = state;
    }
} 