#-*- coding:utf-8 -*-

import random
from itertools import permutations


p = permutations([0, 1, 2, 3, 4, 5, 6]) 
for per in list(p): 
	perm = list(per)
	W = 7
	out = "L{NTP#AGLCSF.#OAR4A#STOL11__}PYCCTO1N#RS.S"
	res = ['0']*42
	msg = ''
	for i in range(100):
		for j in xrange(0, len(out), W):
			for k in xrange(W):
				res[perm[k]+j] = out[j:j+W][k]
		msg =  ''.join(c for c in res)
		msg = msg[-1:] + msg[:-1]
		msg1 = msg[0:21]
		msg2 = msg[21:42]
		msg = ''
		for i in range(21):
			msg += msg1[i] + msg2[i]
		msg = msg[-1:] + msg[:-1]
		out = msg
	if 'FLAG' in msg:
		print msg


'''
perm = [1, 2, 6, 0, 4, 5, 3]
while len(msg) % (2*W):
    msg += "."

for i in xrange(32):
	msg = msg[1:] + msg[:1]
	msg = msg[0::2] + msg[1::2]
	msg = msg[1:] + msg[:1]
	res = ""
	for j in xrange(0, len(msg), W):
		for k in xrange(W):
			res += msg[j:j+W][perm[k]]
	msg = res
out = msg
'''


