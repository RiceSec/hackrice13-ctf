from Crypto.Util.number import getPrime, bytes_to_long
from secret import flag

e = 3

while True:
    p = getPrime(64)
    q = getPrime(64)
    n = p * q
    phi = (p - 1) * (q - 1)

    try:
        d = pow(e, -1, phi)
    except:
        continue

    break

m = bytes_to_long(flag)

assert m < n

c = pow(m, e, n)

print("make sure to wrap the flag in the hackrice{}")
print()

print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")
