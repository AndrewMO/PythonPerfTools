# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import threading


def ssh2(host, username, passwd, cmd):
    try:

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(host, 22, username, passwd, timeout=5)
        ServerNo = host[15:17]

        for m in cmd:

            stdin, stdout, stderr = ssh.exec_command(m)

            # stdin.write("Y")   #简单交互，输入 ‘Y’

            out = stdout.readlines()

            # 屏幕输出

            for o in out:
                #print(o)
                print(" server : %s , Java PID :  %s" % (ServerNo, o))

        #print('%s\t start service OK\n' %(host))

        ssh.close()

    except:

        print('%s\tError\n' %(host))


if __name__ == '__main__':

    cmd = ['ps -ef|grep java|grep -v grep|grep ActiveNetServlet1|awk \'{print $2}\'']  # 你要执行的命令列表

    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码

    threads = []  # 多线程

    print("Begin......")

    for i in range(1, 19):

        if i < 10:
            host1 = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
        else:
            host1 = 'perf-activenet-' + str(i) + 'w.an.active.tan'



        a = threading.Thread(target=ssh2, args=(host1, username, passwd, cmd))
        a.start()


