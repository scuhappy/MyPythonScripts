import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://www.douban.com")

fo = open('E:/PythonScripts/Test.html','wb')
fo.write(html)