#https://github.com/kmyk/mersenne-twister-predictor
from mt19937predictor import MT19937Predictor
from pwn import *

predictor = MT19937Predictor()
conn = process('./prediction.py') #change it to remote
for i in range(3):
	conn.recvuntil("Random Number is :")
	print ("Receiving the random number "+str(i))
	rnd_number=int(conn.recvline())
	predictor.setrandbits(rnd_number,32)

for i in range(624):
	conn.sendline("0123456789")
	conn.recvuntil("was :")
	rnd_number=int(conn.recvline().strip())
	predictor.setrandbits(rnd_number,32)

try:
	for i in range(40):
		predicted=predictor.getrandbits(32)
		print ("The predicted number is : "+str(predicted))
		conn.sendline(str(predicted))
		print (conn.recvline())
	print (conn.recvline())
	print (conn.recvline())
	print (conn.recvline())
except:
	print ("I think its the end!!")
	print (conn.recvline())

