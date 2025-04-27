/**
 * 优惠券状态枚举
 */
public enum CouponStateEnum {
    
    UNUSED(1, "未使用"),
    USED(2, "已核销"),
    INVALID(3, "作废"),
    FROZEN(4, "冻结"),
    EXPIRED(5, "过期");

    private final Integer code;
    private final String description;

    CouponStateEnum(Integer code, String description) {
        this.code = code;
        this.description = description;
    }

    public Integer getCode() {
        return code;
    }

    public String getDescription() {
        return description;
    }

    /**
     * 根据状态码获取枚举
     * @param code 状态码
     * @return 对应的枚举值，如果未找到则返回null
     */
    public static CouponStateEnum getByCode(Integer code) {
        if (code == null) {
            return null;
        }
        for (CouponStateEnum state : values()) {
            if (state.getCode().equals(code)) {
                return state;
            }
        }
        return null;
    }

    /**
     * 判断状态码是否有效
     * @param code 状态码
     * @return 是否是有效的状态码
     */
    public static boolean isValidCode(Integer code) {
        return getByCode(code) != null;
    }

    /**
     * 获取状态描述
     * @param code 状态码
     * @return 状态描述，如果状态码无效则返回null
     */
    public static String getDescriptionByCode(Integer code) {
        CouponStateEnum state = getByCode(code);
        return state != null ? state.getDescription() : null;
    }
} 