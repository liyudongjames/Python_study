import requests
from time import sleep

url = 'http://bailiteng.zhibocloud.cn/api/v2/fare/telCheck'
url2 = 'http://app.qj622.com/api/v2/wallet/recharge'
values = {'mobile': '18681234706',
          'pervalue': '10.00'}
values2 = {'type': 'alipay',
           'amount': '1000.0'}
url3 = 'http://app.qj622.com/api/v2/wallet/charges/19579'

# r = requests.patch(url2, data=values2)
while 1 == 1:
    rll = requests.get(url3)
    print(rll.text)
    sleep(3)
