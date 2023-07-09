from secret import flag, key

enc_flag = [ord("a") + ((ord(c) + key) % 26) for c in flag]
print(f"Encrypted flag: hackrice{{{''.join([chr(c) for c in enc_flag])}}}")
