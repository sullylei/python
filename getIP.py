import socket

def get_ip_list(domain): # 获取域名解析出的IP列表
  ip_list = []
  try:
    addrs = socket.getaddrinfo(domain, None)
    for item in addrs:
      if item[4][0] not in ip_list:
       ip_list.append(item[4][0])
  except Exception as e:
    # print(str(e))
    pass
  return ip_list


if __name__ == "__main__":
 ip_list = get_ip_list("openapi.alipay.com")
 ip_list1 = set(["110.75.236.202","110.75.244.16","110.76.18.202","110.75.231.202","110.75.244.202"])
 for ip_temp in ip_list:
  print(ip_temp)
 temp1=set(ip_list) | ip_list1
 if ip_list1 == temp1:
   print('IP NOT CHANGE')
 else:
   print('IP has changed')
   print(temp1)
