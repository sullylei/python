import urllib.request
#获取request
request = urllib.request.Request("http://placekitten.com/g/600/800")
#得到响应
response = urllib.request.urlopen(request)
#获取图片
cat_img = response.read()
#图片写到本地文件
with open('cat_600_800.jpg','wb') as f:
    f.write(cat_img)
