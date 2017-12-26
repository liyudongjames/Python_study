# 序列化 存储

import pickle

d = dict(name='David', age=24, learning="python")
f = open('io_test', 'wb')

pickle.dump(d, f)
f.close()

with open('Adict', 'wb') as fs:
    pickle.dump(d, fs)