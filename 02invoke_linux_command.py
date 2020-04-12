#getpass是隐藏密码
import paramiko,getpass

def ssh_connect(host_ip,user_name,host_port,password):
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    try:
        ssh.connect(host_ip, host_port, user_name, password)
        return ssh
    except Exception as e:
        print("连接ip为{0}的服务器失败，报错内容如下{1}".format(host_ip,e))
    finally:
        ssh.close()


def execute_command(ssh,str_command):
    # 执行命令并获取执行结果
    stdin, stdout, stderr = ssh.exec_command(str_command)
    execute_result = stdout.read()
    print("execute_result:",execute_result)
    return execute_result

def execute_check(ssh,str_command,host_ip):
    execute_result = execute_command(ssh,str_command)
    if execute_result == '':
        print('execute_result is nothing')
    else:
        print("check execute result is：",execute_result)

if __name__ == '__main__':
    host_ip = '192.168.10.152'
    user_name = 'sully'
    host_port ='22'
    password='sully'
    ssh = ssh_connect(host_ip,user_name,host_port,password)
    print('ssh:',ssh)
   # today_command = "echo `date '+%Y%m%d'`"
   # execute_command(ssh,today_command)
    check_command = 'sh /home/sully/bin/check'
    execute_command(ssh,check_command)
    #str_command = 'grep -Ei "warning|mesg|danger" /home/sully/logs/check.20200412.log'
    str_command = 'grep -Ei "mesg|danger" /home/sully/logs/check.20200412.log'
    execute_check(ssh,str_command,host_ip)
    #read_res_command = "cat /home/sully/logs/check.20200412.log"
    #execute_command(ssh,read_res_command)
    ssh.close()