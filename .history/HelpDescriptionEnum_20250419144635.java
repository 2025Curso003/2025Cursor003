/**
 * 助力描述枚举
 */
public enum HelpDescriptionEnum {
    
    CAN_INVITE(1, "您也可以开启活动邀请好友帮你助力哦~"),
    REACH_LIMIT(2, "已达助力次数上限，无法助力"),
    HELP_FULL(3, "来晚啦，助力人数已达标"),
    ALREADY_HELPED(4, "您已成功为Ta助力啦，无法重复助力"),
    ACTIVITY_ENDED(5, "活动已经结束了哦～"),
    ACTIVITY_RESTING(6, "活动休息中，请稍后重试～"),
    SPECIFIED_USER_ONLY(7, "指定用户才能助力");

    /**
     * 状态码
     */
    private final Integer code;
    
    /**
     * 描述信息
     */
    private final String description;

    HelpDescriptionEnum(Integer code, String description) {
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
    public static HelpDescriptionEnum getByCode(Integer code) {
        if (code == null) {
            return null;
        }
        for (HelpDescriptionEnum status : values()) {
            if (status.getCode().equals(code)) {
                return status;
            }
        }
        return null;
    }

    /**
     * 获取描述信息
     * @param code 状态码
     * @return 状态描述，如果状态码无效则返回null
     */
    public static String getDescriptionByCode(Integer code) {
        HelpDescriptionEnum status = getByCode(code);
        return status != null ? status.getDescription() : null;
    }

    /**
     * 判断状态码是否有效
     * @param code 状态码
     * @return 是否是有效的状态码
     */
    public static boolean isValidCode(Integer code) {
        return getByCode(code) != null;
    }
} 