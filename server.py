#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import string,os,threading,time,sys
from socket import *


def tou(ss,addr):
    #看看是哪个倒霉蛋上钩
    print('有人上钩了........',addr)
    #按照DPC通信协议接收报头
    while True:
        n = ss.recv(50)
        if not n:
            break
        #接收数据处理
        data = n.decode()
        data = data.split()
        print(data)
        filename = data[0]
        filesize = int(data[1])
        #准备接收文件
        f = open(filename,'wb')
        a= 0
        ap = 1000
        while True:
            if filesize < ap:
                ap = filesize
            date = ss.recv(ap)             
            f.write(date)
            a += len(date)
            size1 = filesize - a
            if size1 < 1000:
                ap = size1
            if size1 == 0:
                break
        f.close()
    ss.close()



#改变当前工作路径到此.py文件的路径
os.chdir(sys.path[0])
#创建套接字
adc = ('127.0.0.1',9420)
sock = socket(AF_INET,SOCK_STREAM)
sock.bind(adc)
sock.listen(5)
#使用多线程
while True:
    print('等待中.....')
    ss,addr=sock.accept()
    t = threading.Thread(target=tou,args=(ss,addr))
    t.start()