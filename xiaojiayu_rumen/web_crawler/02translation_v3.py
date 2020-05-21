import urllib.request
import urllib.parse
import json
import time

while True:
    content=input('Enter the word that needs translated（输入q!退出exit ）:')
    if (content == 'q!'):
        break
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'#_o要去掉，否则会出先error_code:50的报错

    #header = {}
    #header['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'


    data={}
    #以下为审查元素，可以在网站翻译页面按F12查看，i和doctype键不可少，其他都可以删除，不影响爬取翻译
    data['i']=content
    data['from']='AUTO'
    data['to']='AUTO'
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    data['salt']='15601659811655'
    data['sign']='78817b046452f9663a2b36604f220360'
    data['doctype']='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action']='FY_BY_REALTTIME'
    data=urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36')

    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')
    target=json.loads(html)
    print('result:%s'%(target['translateResult'][0][0]['tgt']))
    time.sleep(3)
