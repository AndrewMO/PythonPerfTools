# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import datetime
import threading

def upload(host, username, passwd,  src, des):
    try:

        trans = paramiko.Transport((host, 22))
        trans.connect(username=username, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(trans)
        print(' upload file on %s Start %s ' %( host, datetime.datetime.now()))
        # files = os.listdir(src)
        # for f in files:
        #         sftp.put(os.path.join(src,f),os.path.join(des,f))

        sftp.put(src,des)

        print('upload file on %s End %s ' % (host, datetime.datetime.now()))


        trans.close()

    except Exception as e:

        print('%s\t connect  error\n' %(host))
        print("-----------ExceptLog-----------")
        print(e)


if __name__ == '__main__':

    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码

    IgnitecacheXml_srcfile = "D:\\tmp\\0128\\cacheserver\\ignite-cache.xml"

    IgnitecacheXml_desfile = "/opt/active/sites/ignite01/ActiveNetServlet/config/ignite-cache.xml"

    ServiceProperties_srcfile = "D:\\tmp\\0128\\cacheserver\\service.properties"

    ServiceProperties_desfile = "/opt/active/sites/ignite01/ActiveNetServlet/config/service.properties"


    threads = []  # 多线程

    print("Begin......")

    for i in range(1, 3):

        if i < 10:
            host = 'perf-ignite-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-ignite-' + str(i) + 'w.an.active.tan'

        a = threading.Thread(target=upload, args=(host, username, passwd,  IgnitecacheXml_srcfile, IgnitecacheXml_desfile))
        # b = threading.Thread(target=upload, args=(host, username, passwd,  ServiceProperties_srcfile, ServiceProperties_desfile))
        a.start()
        # b.start()
