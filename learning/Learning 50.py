# urllib 访问网络
import json
import urllib
from collections import namedtuple
from urllib import request, parse
import ssl
from OOP.first_json_obj import liao_xue_feng_douban_obj

context = ssl._create_unverified_context()


# 一个简单的http get 请求，其中加入context防止出现unverified错误
# 错误如下
# urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:777)>
# 报错是因为https证书不正确，任何时候都不建议关闭验证，会导致严重的攻击
def get_http():
    with request.urlopen('https://api.douban.com/v2/book/2129650', context=context) as douban:
        data = douban.read()
        print('Status:', douban.status, douban.reason)
        for k, v in douban.getheaders():
            print("%s, %s" % (k, v))
        json_data = data.decode('utf-8')
        print("Data:", json_data)
        return json_data



# 一个带有header的get请求，将我们的请求伪装称为一个iphone6的请求
# 豆瓣将返回给我们一个利于手机页面查看的页面
def get_http_with_header():
    req = request.Request('http://www.douban.com/')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req, context=context) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))


# 一个基本的post请求,登陆微博
def post_http():
    print('Welcome to weibo:')
    email = input('Email:')
    password = input('password:')
    login_data = parse.urlencode([
        ('username', email),
        ('password', password),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])
    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer',
                   'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
    with request.urlopen(req, data=login_data.encode('utf-8'), context=context)as call:
        print('Status:', call.status, call.reason)
        for k, v in call.getheaders():
            print("%s, %s" % (k, v))
        print("datas:", call.read().decode('utf-8'))


# 代理访问
def proxy_http():
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
    opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
    with opener.open('http://www.example.com/login.html') as f:
        # todo 这里写上实现的代码，这部分我自己下去再看吧
        pass


# 网络访问的json变成对象
def get_http_to_object():
    json_data = get_http()
    x = json.loads(json_data, object_hook=lambda d: namedtuple('what', d.keys())(*d.values()))
    print(x)
    print(x.rating)


get_http_to_object()
