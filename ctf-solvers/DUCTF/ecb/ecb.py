from Crypto.Util.number import getPrime, bytes_to_long as b2l, long_to_bytes as l2b, GCD
from Crypto.Util.strxor import strxor
from sympy import invert
from pwn import xor
from Crypto.Cipher import AES
from os import urandom
'''
flag = b"everybodyfuckyou"
KEY = urandom(16)
IV = urandom(16)
print (IV.hex())

def encrypt(msg, key, iv):
	msg = msg + b'\x00'*16
	blocks = [msg[i:i+16] for i in range(0, len(msg), 16)]
	out = b''
	for i, block in enumerate(blocks):
		cipher = AES.new(key, AES.MODE_ECB)
		enc = cipher.encrypt(block)
		if i > 0:
			print(enc.hex())
			enc = strxor(enc, out[-16:])
		out += enc
	return xor(out, iv*(i+1))

def decrypt(ct, key, iv):
	blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]
	out = b''
	for i, block in enumerate(blocks):
		dec = strxor(block, iv)
		if i > 0:
			dec = strxor(dec, ct[(i-1)*16:i*16])
		cipher = AES.new(key, AES.MODE_ECB)
		dec = cipher.decrypt(dec)
		out += dec
	return out

flag = bytes.fromhex("6576657279626f64796675636b796f75")
flag_enc = encrypt(flag, KEY, IV)
print(strxor(flag_enc[:16],flag_enc[16:32]).hex())
flag_dec = decrypt(flag_enc[:16], KEY, IV)
'''
k = b"\x10"*16
print (k.hex())

c = bytes.fromhex("bb84be6699fa0112fc46ac344476767e1dbca6614bc8dd28a9d258dd986c5f55c8171d8f55025aef68801b91fd310a7548e4bcdcf88b68e2be9e70632acc83f30cad26ef1f93c94c7ea71f58002e1d09704b293ac470001b7c26c5c8d29d459e")
iv = bytes.fromhex("aa9032bdb3e0c6a05c56efb4d56d9fe37b5bff987d03bed2c8f36424659ae71e"[32:64])

b1x = c[:16]
b2x = c[16:32]
b3x = c[32:48]
b4x = c[48:64]
b5x = c[64:80]
b6x = c[80:96]
b3 = strxor(strxor(b5x,b6x),iv)
print (b3.hex())

