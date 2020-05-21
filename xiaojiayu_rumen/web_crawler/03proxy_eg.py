import urllib.request
import random

url = 'http://www.whatismyip.com.tw'

iplist = ['119.6.144.73:81','183.203.208.166:8118','111.1.32.28:81']
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
