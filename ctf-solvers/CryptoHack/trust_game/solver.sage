from Crypto.Util.number import bytes_to_long, inverse
from Crypto.Cipher import AES
from json import loads, dumps
from pwn import *

#p = process("./task.py")
p = remote("socket.cryptohack.org", 13396)

# parameters
n = 48
r = 8
a = 0x1337deadbeef
b = 0xb
mod = 2**48

def break_lcg(a, b, p, i, j, outputs):
    deltas = []
    l = b
    o = 1
    for _ in range(8):
        deltas.append(l%p)
        o *= a
        l += o*b
    Y = [(val << (i - j)) for val in outputs]
    k = r
    L = matrix(ZZ, k, k)
    L.set_block(0, 0, -1 * matrix.identity(k))
    L.set_block(0, 0, matrix(ZZ, k, 1, [p, a, a^2, a^3, a^4, a^5, a^6, a^7]))

    B = L.LLL()
    Y = vector([x - y for x, y in zip(Y, deltas)])
    target = vector([ round(RR(w) / p) * p - w for w in B * vector(Y) ])
    states = list(B.solve_right(target))
    return [x + y + z for x, y, z in zip(Y, states, deltas)]

def recover_forward(state):
    recover = []
    s = state
    for i in range(8):
        s = (a * s + b) % mod
        recover.append(s >> 40)
    return bytes(recover).hex()

def recover_backward(state):
    recover = []
    s = int(state)
    for i in range(8):
        s = (s - b)*inverse(a, mod) % mod
        recover.append(s >> 40)
    return bytes(recover[::-1]).hex()


player = p.recvline().decode().split(" ")[5][:-1]
inp = {"option": "get_a_challenge"}
p.sendline(dumps(inp))
data = loads(p.recvline().strip().decode().replace("'",'"'))
plaitnext = data['plaintext']
iv = data['IV']

# forward
seq = []
for i in bytes.fromhex(plaitnext[16:32]):
    seq.append(i)
state = break_lcg(a,b,mod,n,r,seq)[-1]
key_part1 = recover_forward(state)

# backward
seq = []
for i in bytes.fromhex(iv[:16]):
    seq.append(i)
state = break_lcg(a,b,mod,n,r,seq)[0]
key_part2 = recover_backward(state)

key = key_part1 + key_part2

cipher = AES.new(bytes.fromhex(key), AES.MODE_CBC, bytes.fromhex(iv))
c = cipher.encrypt(bytes.fromhex(plaitnext))
inp = {"option": "validate", "ciphertext": c.hex()}
p.sendline(dumps(inp))
print(p.recvline())