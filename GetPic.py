#coding=utf-8
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.png)"'
    imgre = re.compile(reg)
    html = html.decode('utf-8')
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.png' % x)
        x+=1


html = getHtml("http://findicons.com/search/home")

print(getImg(html))