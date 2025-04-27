import re

def extract_verification_code(match_string):
    # 使用正则表达式匹配match='数字'中的数字部分
    pattern = r"match='(\d+)'"
    match = re.search(pattern, match_string)
    if match:
        return match.group(1)
    return None

# 示例使用
match_string = "<re.Match object; span=(175, 181), match='271951'>"
code = extract_verification_code(match_string)
print(f"验证码: {code}")  # 输出: 验证码: 271951 