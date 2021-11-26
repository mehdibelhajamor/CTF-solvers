from pwn import *
from json import loads, dumps
from hashlib import sha256

#conn = process("./mixed.py")
conn = remote("socket.cryptohack.org", 13402)
conn.recvline()

len_flag = 39
flag =""
start = b""
for ll in range(len_flag-1, -1, -1):
	char = ""
	for i in range(8):
		data = start + bytes([1<<i]) + b"\x00"*ll
		ss = {"option": "mix", "data": data.hex()}
		conn.sendline(dumps(ss))
		mixed = loads(conn.recvline().decode().replace("'",'"'))['mixed']

		found = None
		for i in range(256):
			very_mixed = chr(i).encode("latin-1") * len_flag
			super_mixed = sha256(very_mixed).hexdigest()
			if super_mixed == mixed:
				found = "Found"
		if found == None:
			char += "1"
		else:
			char += "0"
	flag += chr(int(char[::-1],2))
	start += b"\x00"
print(flag)
