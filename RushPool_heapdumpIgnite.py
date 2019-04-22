# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import threading


def threaddump(host, username, passwd, getJavaPid, JavaHome, heapdumpfilepath):
    try:

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(host, 22, username, passwd, timeout=5)
        ServerNo = host[12:14]
        JavaPid = -1

        for m1 in getJavaPid:

            stdin, stdout, stderr = ssh.exec_command(m1)

            # stdin.write("Y")   #简单交互，输入 ‘Y’

            out = stdout.readlines()

            # 屏幕输出
            for o in out:
                print(" Java process PID of ' %s ' :  %s" % (host, o))
            JavaPid = ''.join(out).rstrip('\n')


        heapdumpcmd = []
        heapdumpcmd.append('cd ' + JavaHome +';'+'./jmap -dump:format=b,file=' + heapdumpfilepath + '/perfignite' + ServerNo +'heapdump.dump ' + JavaPid)
        #./jmap -dump:format=b,file=/opt/active/ActiveNet/perf/perf18wheapdump.dump  26207

        print("starting heapdump on server %s" %(host))

        for m2 in heapdumpcmd:
            stdin, stdout, stderr = ssh.exec_command(m2)

            # stdin.write("Y")   #简单交互，输入 ‘Y’

            out = stdout.readlines()

            # 屏幕输出
            for o in out:
                print(" heapdump on ' %s ' :  %s" % (host, o))



        print(heapdumpcmd)

        ssh.close()

    except:

        print('%s\tError\n' %(host))


if __name__ == '__main__':

    getJavaPid = ['ps -ef|grep java|grep -v grep|grep ActiveNetServlet1|awk \'{print $2}\'']  # 获取JavaPid的命令
    heapdumpfilepath = "/opt/active/ActiveNet/perf" #dump文件存放路径
    JavaHome = "/usr/java/jdk8-1.8.0_31/bin" # 进入java路径

    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码

    threads = []  # 多线程

    print("Begin......")

    for i in range(1, 3):

        if i < 10:
            host1 = 'perf-ignite-0' + str(i) + 'w.an.active.tan'
        else:
            host1 = 'perf-ignite-' + str(i) + 'w.an.active.tan'



        a = threading.Thread(target=threaddump, args=(host1, username, passwd, getJavaPid, JavaHome, heapdumpfilepath))
        a.start()


