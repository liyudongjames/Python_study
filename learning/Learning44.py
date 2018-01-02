# base64

import base64

# 直接像下面这样去操作可能会抛出 binascii.Error: Incorrect padding的错误，
# 这个错误是因为没有字符自动补齐的原因 解决方法写在def fix_incorrect_padding中
string_what = b"music won't stop"  # 字符串前面加b表示二进制
print(base64.b64encode(string_what))


def fix_incorrect_padding(correct_64):
    correct_64 = b"music won't stop"
    missing_padding = len(correct_64) % 4
    if missing_padding != 0:
        correct_64 += b'=' * (4 - missing_padding)
    return base64.b64encode(correct_64)


print(fix_incorrect_padding(string_what))