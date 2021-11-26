from base64 import b64encode, b64decode
import hashpumpy
from pwn import *

for secret_size in range(1,20):
	print(secret_size)
	append = b"&admin=True&access_sensitive=True&entrynum=7"
	original_hash = b"24c530fdc28030994079df040a64c18466c1cb2d"
	known_data = b"admin=False&access_sensitive=False&author=mehdi&note=haha&entrynum=783"
	new_hash, new_msg = hashpumpy.hashpump(original_hash, known_data, append, secret_size)
	bbb = b64encode(new_msg.decode('ISO-8859-1').encode('unicode-escape'))
	token = "curl -X POST -F 'id="+str(bbb.decode())+"' -F 'integrity="+new_hash+"' crypto.chal.csaw.io:5003/view"
	os.system(token)
	
	
