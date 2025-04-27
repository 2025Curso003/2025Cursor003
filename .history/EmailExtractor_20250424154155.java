import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class EmailExtractor {
    
    /**
     * 从URL中提取邮箱地址
     * @param urls URL列表
     * @return 邮箱地址列表
     */
    public static List<String> extractEmails(List<String> urls) {
        List<String> emails = new ArrayList<>();
        // 定义邮箱参数的正则表达式
        Pattern pattern = Pattern.compile("email=([^&]+)");
        
        for (String url : urls) {
            Matcher matcher = pattern.matcher(url);
            if (matcher.find()) {
                emails.add(matcher.group(1));
            }
        }
        
        return emails;
    }

    public static void main(String[] args) {
        List<String> urls = new ArrayList<>();
        urls.add("https://00mail.cn/prod-api/email/api/stand/getNewEmailContent?email=CruzRichard4717@outlook.com");
        urls.add("https://00mail.cn/prod-api/email/api/stand/getNewEmailContent?email=MillerCheryl9633@outlook.com");
        urls.add("https://00mail.cn/prod-api/email/api/stand/getNewEmailContent?email=MedinaLaura5066@outlook.com");
        urls.add("https://00mail.cn/prod-api/email/api/stand/getNewEmailContent?email=DaltonSarah1488@outlook.com");
        urls.add("https://00mail.cn/prod-api/email/api/stand/getNewEmailContent?email=HudsonMichele1652@outlook.com");
        
        List<String> emails = extractEmails(urls);
        System.out.println("提取的邮箱地址：");
        emails.forEach(System.out::println);
    }
} 