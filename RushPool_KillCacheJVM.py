# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import threading


def threaddump(host, username, passwd, getJavaPid, checkJVM):
    try:

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(host, 22, username, passwd, timeout=5)
        ServerNo = host[15:17]
        JavaPid = -1

        for m1 in getJavaPid:

            stdin, stdout, stderr = ssh.exec_command(m1)

            # stdin.write("Y")   #简单交互，输入 ‘Y’

            out = stdout.readlines()
            if len(out) == 0:
                raise ValueError('JavaPid is null')

            # 屏幕输出
            for o1 in out:
                print(" Java process PID of ' %s ' :  %s" % (host, o1))
            JavaPid = ''.join(out).rstrip('\n')

        killJVMcmd = []
        killJVMcmd.append('kill -9 ' + JavaPid )
        print(killJVMcmd)

        for m2 in killJVMcmd:
            stdin, stdout, stderr = ssh.exec_command(m2)

            # stdin.write("Y")   #简单交互，输入 ‘Y’

            out = stdout.readlines()

            # 屏幕输出
            for o2 in out:
                print(" server ' %s ' :  %s" % (host, o2))


        for m3 in checkJVM:
            stdin, stdout, stderr = ssh.exec_command(m3)
            out = stdout.readlines()
            for o3 in out:
                print(" server ' %s ' :  %s" % (host, o3))

        ssh.close()

    except Exception as e:

        print('%s\tError\n : %s' % (host, e))


if __name__ == '__main__':

    getJavaPid = ['ps -ef|grep java|grep -v grep|grep ActiveNetServlet1|awk \'{print $2}\'']  # 获取JavaPid的命令
    checkJVM = ['ps -ef|grep java|grep -v grep|grep ActiveNetServlet1']  # 检查JVM状态
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

        a = threading.Thread(target=threaddump, args=(host1, username, passwd, getJavaPid, checkJVM))
        a.start()


