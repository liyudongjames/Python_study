# 摘要算法 hashlib 单项加密

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode("utf-8"))
print(md5.hexdigest())

# 数据量过大的时候分开update最后计算的结果都是一样的
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
md52 = hashlib.md5()
md52.update('how to use md5 in '.encode('utf-8'))
md52.update('python hashlib?'.encode('utf-8'))
print(md52.hexdigest())

# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
