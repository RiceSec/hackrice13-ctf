from pwn import *
from Crypto.Util.number import long_to_bytes
from sage.all import factor

p = process(["python", "russia.py"])
p.recvline()
p.recvline()

p.recvuntil(b"n = ")
n = int(p.recvline().strip())

p.recvuntil(b"e = ")
e = int(p.recvline().strip())

p.recvuntil(b"c = ")
c = int(p.recvline().strip())

a, b = factor(n)
phi = (a[0] - 1) * (b[0] - 1)
d = pow(e, -1, phi)

m = pow(c, d, n)
flag = long_to_bytes(m)
print(f"hackrice{{{flag.decode()}}}")
