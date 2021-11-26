from pwn import *
from Crypto.Util.number import long_to_bytes as l2b

guess = []
while True:
	l = 0
	conn = remote("crypto.chal.csaw.io",5001)
	data = conn.readline()
	data = conn.readline()
	while True:
		l+=1
		print l
		try:
			inp = "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
			conn.sendline(inp)
			cipher = conn.readline().strip()
			cipher = cipher[16:]
			c1 = cipher[0:32]
			c2 = cipher[32:64]
			c3 = cipher[64:96]
			data = conn.readline().strip()
			if c1 == c2 and c2 == c3:
				conn.sendline('ECB')
				guess.append('ECB')
			else:
				conn.sendline('CBC')
				guess.append('CBC')
			data = conn.readline().strip()
		except:
			conn.close()
			break
	break
print guess
flag = ''
for i in guess:
	if i == 'ECB':
		flag += '0'
	else:
		flag += '1'
print l2b(int(flag,2))
