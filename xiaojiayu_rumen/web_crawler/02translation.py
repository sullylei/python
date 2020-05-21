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
