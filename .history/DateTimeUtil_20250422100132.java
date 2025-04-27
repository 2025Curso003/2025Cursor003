import cn.hutool.core.date.DateUtil;
import cn.hutool.core.date.DateTime;

/**
 * 日期时间工具类
 */
public class DateTimeUtil {
    
    /**
     * 获取当前时间，格式为yyyyMMddHHmmss的Long类型数字
     * @return 当前时间的Long类型数字
     */
    public static Long getCurrentTimeLong() {
        // 使用Hutool的DateUtil获取当前时间并格式化
        DateTime now = DateUtil.date();
        String timeStr = DateUtil.format(now, "yyyyMMddHHmmss");
        // 转换为Long类型
        return Long.parseLong(timeStr);
    }

    /**
     * 简单使用方式
     */
    public static void main(String[] args) {
        Long currentTime = getCurrentTimeLong();
        System.out.println("当前时间: " + currentTime);
        // 输出示例：当前时间: 20250417143022 (2025年04月17日14时30分22秒)
    }
} 