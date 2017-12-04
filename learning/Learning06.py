import urllib.request

url = "http://www.baidu.com"
http_response = urllib.request.urlopen(url)
data = http_response.read()
data = data.decode('UTF-8')
print(data)
