from pwn import *
import time
conn = remote("secretarray.fword.wtf", 1337)

data = conn.recvuntil("START:").strip()
conn.recvline().strip()

i = 0
j = 1
k = 2

array = []

while True:
	msg1 = str(i) + ' ' + str(j)
	msg2 = str(j) + ' ' + str(k)
	msg3 = str(i) + ' ' + str(k)

	conn.sendline(msg1)
	x = int(conn.recvline().strip())

	conn.sendline(msg2)
	y = int(conn.recvline())

	conn.sendline(msg3)
	z = int(conn.recvline())

	a = (x-y+z)/2
	b = x-a
	c = z-a

	assert a + b == x
	assert b + c == y
	assert c + a == z

	array.append(a)
	array.append(b)
	array.append(c)
	
	i += 3
	j += 3
	k += 3

	if k == 1337:
		i = 1334

		msg1 = str(i) + ' 1335'
		msg2 = str(i) + ' 1336'


		conn.sendline(msg1)
		x = int(conn.recvline().strip())
		
		conn.sendline(msg2)
		y = int(conn.recvline())

		a = array[i]
		b = x-a
		c = y-a

		assert a + b == x
		assert a + c == y

		array.append(b)
		array.append(c)
		break
	

req = "DONE"
for i in array:
	req = req + ' ' + str(i)
conn.sendline(req)
conn.interactive()
