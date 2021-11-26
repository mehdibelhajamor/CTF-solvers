def bxor(a1, b1):
    encrypted = [ (a ^ b) for (a, b) in zip(a1, b1) ]
    return bytes(encrypted)

mac = "97ade8554ecf57d47496e3541dc1832269ec406fcbea9c5fd2176753e350b446"
iv = bytes.fromhex(mac[32:])
t = bytes.fromhex(mac[:32])
my_msg = b"flagflagflagflag"

bit_flip = bxor(b"cashcashcashcash",b"flagflagflagflag")
iv = bxor(iv, bit_flip)

print(t.hex() + iv.hex())

#DUCTF{WAT_I_THOUGHT_IV_IZ_G00D}