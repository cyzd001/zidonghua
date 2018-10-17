import paramiko

# 初始化一个paramiko的Socket对象
trans = paramiko.Transport(('192.168.55.26', 22))
# 建立基于Socket的ssh2连接
trans.connect(username='root', password='abc.abc')
# 建立SSH服务器的高级会话
ssh = paramiko.SSHClient()
# 将Socket连接赋与ssh会话
ssh._transport = trans
# 通过SSH会话执行命令
stdin,stdout,stderr = ssh.exec_command("/usr/tomcat/bin/catalina.sh start")   #重启tomcat命令

print(stdout.read())
# print('------------------')
# print(stdout.read())
# print(stderr.read())
ssh.close()