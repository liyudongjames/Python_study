# 文件读取

import pickle


with open('io_test', 'rb') as fs:
    d = pickle.load(fs)

print(d)