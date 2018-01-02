# 二进制转换 struct

import struct

byts_num = struct.pack(">I", 1231231123)  # >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
print(byts_num)

number = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(number)
