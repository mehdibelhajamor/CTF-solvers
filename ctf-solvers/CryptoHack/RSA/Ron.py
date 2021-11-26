from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l, isPrime
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from gmpy2 import gcd
from sympy import invert

keys = []
for i in range(0,50):
	key = RSA.importKey(open(str(i+1)+'.pem').read())
	e = key.e
	n = key.n
	c = int(open(str(i+1)+'.ciphertext').readline().strip(),16)
	keys.append([n,e,c,i+1])

N = 1
for key in keys:
	N *= key[0]

for key in keys:
	g = gcd(key[0],N//key[0])
	if g!=1 and key[3]==21:
		n = key[0]
		e = key[1]
		c = l2b(key[2])
		p = g
		q = n/p
		phi = (p-1)*(q-1)
		d = int(invert(e,phi))

		key = RSA.construct((n, long(e), d))
		cipher = PKCS1_OAEP.new(key)

		print cipher.decrypt(c)