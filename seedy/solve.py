from pwn import *

r = process("python seedy.py", shell=True)
r.readline()
r.readuntil(b"spaces: ")

r.sendline(b"831878")
r.readuntil(b"you won!\n")

flag = r.readline()
sys.stdout.buffer.write(flag)
