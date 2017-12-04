import re
import urllib
import requests


def get_html(url):
    rll = requests.get(url)
    text = rll.text()
    return text


def get_img(text):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, text)
    return imglist


text = get_html("http://tieba.baidu.com/p/2460150866")
print (get_img(text))