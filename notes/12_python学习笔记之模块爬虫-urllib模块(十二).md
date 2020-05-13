# 一.python如何访问互联网
## 1.1 urllib模块介绍
url + lib 组成了urllib模块

通过urllib访问百度首页示例：
```bash
>>> import urllib.request as req
>>> response = req.urlopen('http://www.baidu.com')
>>> html = response.read()
>>> html = html.decode('utf-8')
>>> print(html)
```
## 1.2 爬取一只猫的图片
访问http://placekitten.com网站，获取一张600*800的jpg图片
示例代码如下：

```bash
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

```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200513081053834.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N1bGx5MjAwOA==,size_16,color_FFFFFF,t_70#pic_center)
# 二.通过有道词典来翻译
## 2.1 查看网页版有道词典
在浏览器中输入：http://fanyi.youdao.com/，同时按下F12,打开开发者工具
查看network页签中的内容，如下图
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200514000346646.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N1bGx5MjAwOA==,size_16,color_FFFFFF,t_70)
查看http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule	请求页签中的request url和from data区域
![from data](https://img-blog.csdnimg.cn/20200514000546885.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N1bGx5MjAwOA==,size_16,color_FFFFFF,t_70)
## 2.2 通过python来实现翻译

```bash
import urllib.request
import urllib.parse
import json

content=input('Enter the word that needs translated:')
#http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
#translate_o要改成translate
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15893844176578'
data['sign'] = '33d74a960c3e39c6eb93bc725324a233'
data['ts']='1589379361257'
data['bv']='0ea2f265e69dc7094ed5f0b64ef39e0b'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTlME'

data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)

html = response.read().decode('utf-8')

target=json.loads(html)
print('result:%s'%(target['translateResult'][0][0]['tgt']))
```
http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule请求的url中需去掉_o
