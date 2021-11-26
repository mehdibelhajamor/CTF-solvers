from Crypto.Util.number import bytes_to_long, long_to_bytes
from pwn import *
import base64
import codecs
import json

conn = remote("socket.cryptohack.org",13377)

while True:
	cipher = json.loads(conn.recvline().decode())

	if 'flag' in cipher:
		print cipher["flag"]
		break

	enc = cipher["encoded"]
	typ = cipher["type"]

	if typ == "base64":
		encoded = base64.b64decode(enc.encode()).decode()
	elif typ == "hex":
		encoded = enc.decode('hex')
	elif typ == "rot13":
		encoded = codecs.decode(enc, 'rot_13')
	elif typ == "bigint":
		encoded = enc[2:].decode('hex')
	elif typ == "utf-8":
		encoded = ''.join(chr(b) for b in enc)
	
	to_send = '{"decoded": "'+encoded+'"}'
	print to_send

	conn.sendline(to_send)