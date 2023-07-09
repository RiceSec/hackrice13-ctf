import random
from pwn import *
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

r = process(["python", "mallory.py"])

r.recvuntil(b"p = ")
p = int(r.recvline())

r.recvuntil(b"g = ")
g = int(r.recvline())
r.recvline()

r.recvuntil(b"A = ")
a = int(r.recvline())

r.recvuntil(b"A' = ")
alice_private_fake = random.randrange(2, p - 1)
alice_public_fake = pow(g, alice_private_fake, p)

r.sendline(str(alice_public_fake).encode())
r.recvline()

r.recvuntil(b"B = ")
b = int(r.recvline())

r.recvuntil(b"B' = ")
bob_private_fake = random.randrange(2, p - 1)
bob_public_fake = pow(g, bob_private_fake, p)

r.sendline(str(bob_public_fake).encode())
r.recvline()

alice_shared_k = pow(a, bob_private_fake, p)
bob_shared_k = pow(b, alice_private_fake, p)

print(alice_shared_k, bob_shared_k)

alice_shared_key = alice_shared_k.to_bytes(16, "big")
bob_shared_key = bob_shared_k.to_bytes(16, "big")

r.recvuntil(b"= ")
a2b_ciphertext_bytes = bytes.fromhex(r.recvline().strip().decode())
bob_cipher = AES.new(alice_shared_key, AES.MODE_ECB)
a2b_plaintext = unpad(bob_cipher.decrypt(a2b_ciphertext_bytes), 16)

print(r.recvuntil(b"as hex: "))
bob_cipher = AES.new(bob_shared_key, AES.MODE_ECB)
a2b_ciphertext_mod = bob_cipher.encrypt(pad(a2b_plaintext, 16))

r.sendline(a2b_ciphertext_mod.hex().encode())
print(r.recvline())

print(r.recvuntil(b"= "))
stuff = r.recvline()
print(stuff)
b2a_ciphertext_bytes = bytes.fromhex(stuff.strip().decode())
alice_cipher = AES.new(bob_shared_key, AES.MODE_ECB)
b2a_plaintext = unpad(alice_cipher.decrypt(b2a_ciphertext_bytes), 16)

print(r.recvuntil(b"as hex: "))
alice_cipher = AES.new(alice_shared_key, AES.MODE_ECB)
b2a_ciphertext_mod = alice_cipher.encrypt(pad(b2a_plaintext, 16))
r.sendline(b2a_ciphertext_mod.hex().encode())
print(r.recvline())

print(r.recvuntil(b"= "))
flag_ciphertext = bytes.fromhex(r.recvline().strip().decode())
alice_cipher = AES.new(alice_shared_key, AES.MODE_ECB)
flag_plaintext = unpad(alice_cipher.decrypt(flag_ciphertext), 16)
print(flag_plaintext)
