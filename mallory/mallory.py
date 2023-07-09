import random
from Crypto.Util.number import getPrime
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from sympy.ntheory.residue_ntheory import primitive_root
from secret import flag

p = getPrime(128)
g = primitive_root(p)

print(f"p = {p}")
print(f"g = {g}")

print("================")

alice_private = random.randrange(2, p - 1)
alice_public = pow(g, alice_private, p)
print(f"A = {alice_public}")

alice_public_fake = int(input("A' = "))

print("================")

bob_private = random.randrange(2, p - 1)
bob_public = pow(g, bob_private, p)
print(f"B = {bob_public}")

bob_public_fake = int(input("B' = "))

print("================")

alice_shared_k = pow(bob_public_fake, alice_private, p)
bob_shared_k = pow(alice_public_fake, bob_private, p)

alice_shared_key = alice_shared_k.to_bytes(16, "big")
bob_shared_key = bob_shared_k.to_bytes(16, "big")

alice_cipher = AES.new(alice_shared_key, AES.MODE_ECB)
a2b_plaintext = random.randbytes(16)
a2b_ciphertext = alice_cipher.encrypt(pad(a2b_plaintext, 16))
print(f"ciphertext (alice to bob) = {a2b_ciphertext.hex()}")
assert (
    unpad(AES.new(alice_shared_key, AES.MODE_ECB).decrypt(a2b_ciphertext), 16)
    == a2b_plaintext
)

a2b_ciphertext_fake = input("enter ciphertext that bob should receive as hex: ")
a2b_ciphertext_fake_bytes = bytes.fromhex(a2b_ciphertext_fake)
bob_cipher = AES.new(bob_shared_key, AES.MODE_ECB)
stuff = bob_cipher.decrypt(a2b_ciphertext_fake_bytes)
assert unpad(stuff, 16) == a2b_plaintext
print("================")

bob_cipher = AES.new(bob_shared_key, AES.MODE_ECB)
b2a_plaintext = random.randbytes(16)
b2a_ciphertext = bob_cipher.encrypt(pad(b2a_plaintext, 16))
print(f"ciphertext (bob to alice) = {b2a_ciphertext.hex()}")

b2a_ciphertext_fake = input("enter ciphertext that alice should receive as hex: ")
b2a_ciphertext_bytes_fake = bytes.fromhex(b2a_ciphertext_fake)
alice_cipher = AES.new(alice_shared_key, AES.MODE_ECB)
assert unpad(alice_cipher.decrypt(b2a_ciphertext_bytes_fake), 16) == b2a_plaintext
print("================")

a2b_ciphertext = alice_cipher.encrypt(pad(flag.encode(), 16))
print(f"ciphertext (alice to bob) = {a2b_ciphertext.hex()}")
