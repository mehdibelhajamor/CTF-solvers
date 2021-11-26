
import sys
from struct import pack, unpack
from Crypto.Util.number import long_to_bytes as l2b

def F(w):
	return ((w * 31337) ^ (w * 1337 >> 16)) % 2**32

def encrypt(block):
	a, b, c, d = unpack("<4I", block)
	for rno in xrange(32):
		a, b, c, d = b ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d), c ^ F(a ^ F(d) ^ (a | d)), d ^ F(a | F(a) ^ a), a ^ 31337
		a, b, c, d = c ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a), b ^ F(d ^ F(a) ^ (d | a)), a ^ F(d | F(d) ^ d), d ^ 1337
	return pack("<4I", a, b, c, d)

def decrypt(block):
	a, b, c, d = unpack("<4I", block)
	for rno in xrange(32):

		nd = d ^ 1337
		na = c ^ F(nd | F(nd) ^ nd)
		nb = b ^ F(nd ^ F(na) ^ (nd | na))
		nc = a ^ F(nd | F(nb ^ F(na)) ^ F(nd | nb) ^ na)

		a = nd ^ 31337
		d = nc ^ F(a | F(a) ^ a)
		c = nb ^ F(a ^ F(d) ^ (a | d))
		b = na ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d)

	return pack("<4I", a, b, c, d)

ct = open("flag.enc","r+").read()
print ct
fl = "".join(decrypt(ct[i:i+16]) for i in xrange(0, len(ct), 16))
print fl
