import os

namelist = {'www.51cto.com':'218.11.0.91','www.51talk.com':'60.205.82.82'}

mail = ['bliu@test.cn','smcao@test.cn']

def check_domain():
        '''使用nslook域名解析并与字典ip对比，如果解析异常发邮件给指定收件人'''
        for i in namelist:
                address = os.popen("nslookup %s | grep -v '#53' | awk -F':' '/^Address/{print $2}'" % i).read().strip()
                if (address == namelist[i]):
                        pass
                else:
                                os.system('echo "%s域名解析异常,解析的地址为%s,$(date)" >> /var/log/dns_error.log'%(i,address))
                        for j in mail:
                                os.popen("echo '%s域名解析异常，请确认！'| mail -s '%s域名解析异常' %s" %(i,i,j))
                                #os.popen括号中百分号后面的i,i,j分别是将python的指定变量传到shell命令中


check_domain()