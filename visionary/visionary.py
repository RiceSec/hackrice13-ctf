from secret import secret, key

normalized_secret = "".join([c.upper() for c in secret if c.isalpha()])
normalized_key = "".join([c.upper() for c in key if c.isalpha()])

encrypted = ""
for i, c in enumerate(normalized_secret):
    k = normalized_key[i % len(normalized_key)]
    encrypted += chr((ord(c) + ord(k)) % 26 + 65)

print(encrypted)
