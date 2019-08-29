#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by WenBin2019-08-06 11:05:20


from Crypto.Cipher import AES
import os,sys
def jiemi(abk):
        obj = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456'    )
        try:
                with open(abk,'rb') as f:
                        data = f.read()        
        except FileNotFoundError:
                sys.exit(1)
                pass
        
        os.remove(abk)
        mass = data
        ciphertext = obj.decrypt(mass)
        ciphertext = ciphertext.rstrip(bytes("\0" ,encoding = 'utf-8'))
        with open(abk,'wb') as f:
                f.write(ciphertext)
        print(ciphertext)

#遍历磁盘


'''
        for c in string.ascii_uppercase:
        drive = c + ':'
        if os.path.isdir(drive):
        drive_list.append(drive)
'''
if __name__ == "__main__":
        for v in ['c:/Users/Administrator/Desktop/机密']:
                for root, dirs, files in os.walk(v):
                        for f in files:
                                if os.path.splitext(f)[1] == '.mp3' or os.path.splitext(f)[1] == '.md' or  os.path.splitext(f)[1] == '.py' or os.path.splitext(f)[1] == '.txt' or os.path.splitext(f)[1] == '.avi' or os.path.splitext(f)[1] == '.mp4' or os.path.splitext(f)[1] == '.rmvb' or os.path.splitext(f)[1] == '.docx':
                                        abk = os.path.join(root,f)
                                        print(abk)
                                        jiemi(abk)
                                        
        

        

