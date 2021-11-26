#-*- coding:utf-8 -*-

import os
import hashlib
import random
import string


msg = open("output").read().strip()
s = string.printable

flag = ''
for i in range(0,len(msg)-96):
	pl = msg[i:i+96]
	try:
		for c1 in s:
			for c2 in s:
				pair = c1+c2
				h = hashlib.sha512(pair).hexdigest()[16:-16][::-1]
				if pl == h:
					flag += pair
	except:
		pass
print flag