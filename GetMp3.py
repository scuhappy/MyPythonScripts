import requests
import urllib
r = requests.get('http://music.163.com/api/playlist/detail?id=3779629')
arr = r.json()['result']['tracks']
for i in range(10): name = str(i+1)+ ' ' + arr[i]['name']+ '.mp3'
link = arr[i]['mp3Url']
urllib.request.urlretrieve(link,'E:/PythonScripts/'+name)
print(name+'Download successfully!')