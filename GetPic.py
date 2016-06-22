#coding=utf-8
import urllib.request
import re
PageNumber =1
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r' <img src="(.*?.png)" alt='
    imgre = re.compile(reg)
    html = html.decode('utf-8')
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        print(imgurl)
        urllib.request.urlretrieve(imgurl,'E:\MyPythonScripts\Icons\\'+str(PageNumber)+'%s.png' % x)
        x+=1
for i in range(20):
	html = getHtml("http://findicons.com/search/home/"+str(i))
	getImg(html)
	PageNumber+=1
	
