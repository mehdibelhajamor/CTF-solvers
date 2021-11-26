from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor

rang = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

test = '▒▒1e▒▒0▒0▒▒▒▒▒9▒▒c▒▒e▒▒2▒▒4▒▒▒▒7'

first_enc_block = 'ed5dd65ef5ac36e886830cf006359b30'
#Solution
"""
msg = 'If Bruce Schneier multiplies two primes, the product is prime. On a completely unrelated note, the key used to encrypt this message is '
pad_block = '\x09'*9
key = '0b9d0fe1920ca685e3851b162b8cc9e5'
msg = (msg + key + pad_block).encode()
blocks = [msg[i:i+16] for i in range(0, len(msg), 16)]
blocks = blocks[::-1]
out = []
enc_block = "0112c744b0aac58207aea28e804ec6ab"
enc_block = bytes.fromhex(enc_block)
c = strxor(enc_block, blocks[10])
Cipher = AES.new(bytes.fromhex(key), AES.MODE_ECB)
c = Cipher.decrypt(c)
c = strxor(c,blocks[9])
c = strxor(c,blocks[11])
c = c.hex()
print('block= ',c)
"""

#final
key = '0b9d0fe1920ca685e3851b162b8cc9e5'
b1 = b"If Bruce Schneie"
f2 = bytes.fromhex("215f6275745f666c3467735f61723321")
E = bytes.fromhex('ed5dd65ef5ac36e886830cf006359b30')
c = strxor(f2,E)
Cipher = AES.new(bytes.fromhex(key), AES.MODE_ECB)
c = Cipher.decrypt(c)
print(strxor(c,b1))

#DUCTF{IVs_4r3nt_s3cret!_but_fl4gs_ar3!}