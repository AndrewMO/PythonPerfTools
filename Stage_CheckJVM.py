# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import threading


def ssh2(host, username, passwd, cmd):
    try:

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(host, 22, username, passwd, timeout=5)

        for m in cmd:

            stdin, stdout, stderr = ssh.exec_command(m)

            # stdin.write("Y")   #简单交互，输入 ‘Y’

            out = stdout.readlines()

            # 屏幕输出

            for o in out:
                #print(o)
                print("%s service status : %s" % (host, o))

        #print('%s\t start service OK\n' %(host))

        ssh.close()

    except Exception as e:

        print('%s\tError\n:' %(host))
        print(e)


if __name__ == '__main__':

    cmd = ['ps -ef|grep java|grep -v grep|grep 19.01.0.067']  # 你要执行的命令列表

    # cmd = ['ps -ef|grep java|grep -v grep']  # 你要执行的命令列表

    # cmd = ['ps -ef|grep java']  # 你要执行的命令列表

    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码

    threads = []  # 多线程

    print("Begin......Servlet")

    for i in range(1, 3):

        #stage-activenet-01w.an.dev.activenetwork.com

        if i < 10:
            host1 = 'stage-activenet-0' + str(i) + 'w.an.dev.activenetwork.com'
        else:
            host1 = 'stage-activenet-' + str(i) + 'w.an.dev.activenetwork.com'

        a = threading.Thread(target=ssh2, args=(host1, username, passwd, cmd))
        a.start()

    print("Begin......Cache")

    for i in range(1, 4):
        #stage-activenet-ignite04w.an.dev.activenetwork.com


        if i < 10:
            host2 = 'stage-activenet-ignite0' + str(i) + 'w.an.dev.activenetwork.com'
        else:
            host2 = 'stage-activenet-ignite' + str(i) + 'w.an.dev.activenetwork.com'

        b = threading.Thread(target=ssh2, args=(host2, username, passwd, cmd))
        b.start()
