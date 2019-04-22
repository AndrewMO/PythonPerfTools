# -*- coding: utf-8 -*-

# !/usr/bin/python


import requests
import threading
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)


def getResponse(url):
    response = requests.get(url)
    # if response.status_code == 200:
    #     status = 'OK'
    # print(response.text)
    rsc = response.status_code
    serverNo = url[22:24]


    print("hosturl : %s ; Number : %s ; Status_Code : %r" % (url, serverNo, rsc))



if __name__ == '__main__' :

    logging.debug('start of program')
    thread = []
    orgname = 'perf01jetty'



    for i in range(1, 19):
        if (i < 10):
            urlstr = "http://perf-activenet-0"+str(i)+"w.an.active.tan:3000/"+orgname+"/servlet/adminlogin.sdi"
            # logging.debug('i is '+ str(i) + ' , url is ' + urlstr)
        else:
            urlstr = "http://perf-activenet-"+str(i)+"w.an.active.tan:3000/"+orgname+"/servlet/adminlogin.sdi"
            # logging.debug('i is ' + str(i) + ' , url is ' + urlstr)
        # print(urlstr)
        # logging.debug("server  %r is initialing" %(i))
        a = threading.Thread(target=getResponse, args=(urlstr,))
        a.start()

        # logging.debug('end of program')





