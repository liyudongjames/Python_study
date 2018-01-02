# hmac 在摘要算法的基础上，有多增加了一个salt口令，在原输入（message）的基础上在多加入一个salt
# （message + salt）防止通过彩虹表根据哈希值反推口令

import hmac

message = b"this is a message"
key = b"secrete"
h = hmac.new(key, message, digestmod="MD5")
hex_mc = h.hexdigest()
print(hex_mc)