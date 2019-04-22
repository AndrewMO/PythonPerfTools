# -*- coding: utf-8 -*-

# !/usr/bin/python


import requests
import threading
from bs4 import BeautifulSoup



def getResponse(url):
    response = requests.get(url)
    rspcode = response.status_code
    serverNo = url[22:24]

    bsObj = BeautifulSoup(response.text, "html.parser")

    # nameList = bsObj.findAll("td", {"class": "green"})

    OrgInfoTable =  bsObj.body.find("table", class_="compact")

    JDKEnv = OrgInfoTable.find_All("tr")




    print("JEKENV :", JDKEnv)




    # print(bsObj.prettify())

    # print("hosturl : %s ; Number : %s ; Status_Code : %r" % (url, serverNo, rsc))



if __name__ == '__main__' :
    thread = []

    for i in range(1, 2):
    # for i in range(1, 19):
        if (i < 10):
            urlstr = "http://perf-activenet-0"+str(i)+"w.an.active.tan:3000/acm01vegasjetty/servlet/version.sdi"
        else:
            urlstr = "http://perf-activenet-"+str(i)+"w.an.active.tan:3000/acm01vegasjetty/servlet/version.sdi"
        # print(urlstr)
        # print("server  %r is initialing"  %(i))
        a = threading.Thread(target=getResponse, args=(urlstr,))
        a.start()

        # logging.debug('end of program')





