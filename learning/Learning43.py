# collections

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter


Point = namedtuple("point", ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

dd = deque(['a', 'b', 'c'])
print(dd)
dd.append('2')
print(dd)
dd.appendleft('3')
print(dd)

Circle = namedtuple('Circle', ['x', 'y', 'z'])
yuan = Circle(x=10, y=10, z=10)
print(yuan)

# defaultdict dict默认的key
null_by_nul = defaultdict(default_factory='NULL')
null_by_nul['key1'] = 'fanfan'
null_by_nul['key2'] = 'renzhong'

print(null_by_nul.get('key1'))
print(null_by_nul.get('key2'))
print(null_by_nul.get('key3'))

order_null = dict([('a', 1), ('b', 4), ('c', 3)])
print(order_null)

# OrderDict提供一个插入顺序的dict，当容量超出限制，先删除最早添加的那个key
order_null = OrderedDict([('a', 1), ('c', 4), ('b', 3)])
print(order_null)

c = Counter() # Counter 计数器
for ch in 'programing':
    c[ch] = c[ch] + 1

print(c)

