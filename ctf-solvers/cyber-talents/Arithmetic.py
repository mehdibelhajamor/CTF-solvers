from hashlib import sha256


ct = open("ciphertext").read().strip().decode('hex')
c = ct[0]
f = ord('F')


for op in range(0,4):
	for v in range(256):
		for i in xrange(32):
			if (ord('F') + v) % 256 == ord(c):
				print "op = 0"
				print v
			elif (ord('F') ^ v) % 256 == ord(c):
				print "op = 1"
				print v
			elif (ord('F') - v) % 256 == ord(c):
				print "op = 2"
				print v
			elif (ord('F') * (v | 1)) % 256 == ord(c):
				print "op = 3"
				print v
