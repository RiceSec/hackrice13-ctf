import hashlib

def check_flag(flag):
    r = [11414250, 12784543, 11233715, 3457197, 13108470, 5977344, 2358976, 12061037, 1504289, 687684, 13842736, 5263158, 5294618, 7078582, 4493926, 20771, 10851661, 8445149, 16371373, 12383404, 7251101, 15900851, 7586904, 12638492, 12979339]
    v = int.from_bytes(b'QUACK')
    i = 0
    for char in flag:
        v = int.from_bytes(hashlib.sha256(int.to_bytes([lambda x,y:x+y,lambda x,y:x-y,lambda x,y:x*y,lambda x,y:1000000*x-42*y,][i%4](v,ord(char)),16)).digest()[:3])
        if v != r[i]:
            return False
        i += 1
    return i == 25

print('Please enter your password:')
if check_flag(input()):
    print('Welcome!')
else:
    print('Incorrect!')
