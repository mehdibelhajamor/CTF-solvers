from Crypto.Cipher import AES

key = '\x00'*14
ctxt = '0294c9250b515e1686ba600a0b23d767'
ptxt2, ctxt2 = '23df1b9f02d5d50702bfc77f0328dd94', 'a6a28395f882097d1f542db61ee2a4bd'
def decode(flag, k1, k2):
	cipher1 = AES.new(k1, AES.MODE_ECB)
	cipher2 = AES.new(k2, AES.MODE_ECB)
	fl = cipher2.decrypt(flag.decode('hex'))
	msg = cipher1.decrypt(fl)
	return msg
#6523399189690767
cipher_tab = []
keys_tab = []
for i in range(256):
	for j in range(256):
		for l in range(256):
			k = chr(j) + chr(l)
			k1 = key + k
			cipher = AES.new(k1, AES.MODE_ECB)
			enc = cipher.encrypt(ptxt2.decode('hex'))
			cipher_tab.append(enc.encode('hex'))
			keys_tab.append(k1)
	break

for k2 in keys_tab:
	cipher = AES.new(k2, AES.MODE_ECB)
	flag = cipher.decrypt(ctxt2.decode('hex'))
	flag = flag.encode('hex')
	if flag in cipher_tab:
		k1 = keys_tab[cipher_tab.index(flag)]
		msg = decode(ctxt,k1,k2)
		print msg
		exit()
