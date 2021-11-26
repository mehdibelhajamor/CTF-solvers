from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii
from pwn import *
import string
from Crypto.Util.number import bytes_to_long as b2l

s = string.printable

conn = remote('chal.ctf.b01lers.com',2007)
flag = 'flag{brUt3_4ev'
#flag{brUt3_4evR}
for j in s:
	fl = flag + j + '}'
	fl = bin(b2l(fl))
	conn.sendline(fl)
	data = conn.recvline().strip()
	'''
	test = True
	for c in data:
		if c != '0':
			test = False
	'''
	if data == 'True':
		flag = flag + j + '}'
		print flag
		exit()
conn.close()
