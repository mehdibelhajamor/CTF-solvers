from Crypto.Util.number import long_to_bytes

n = 5654655333396589573009251270272824452868045532409847035578809519921971758405056586087615745288
primes = [8,3,157,179,4339,1112581,53693611291973,94333140093961,349904234337911801671,979906911043329098468466567737]

construct = []
for i in range(1024):
	b = bin(i)[2:]
	while len(b)%10 != 0:
		b = '0' + b
	p = 1
	q = 1
	for j in range(len(b)):
		if b[j] == '0':
			p*=primes[j]
		else:
			q*=primes[j]
	assert p*q == n
	construct.append((p,q))

for p,q in construct:
	for i in range(4,11):
		for j in range(4,11):
			const_seq0 = p.digits(i+1)[::-1]
			const_seq1 = q.digits(j+1)[::-1]
			flag = ''
			for k in range(min(len(const_seq1),len(const_seq0))):
				flag += const_seq0[k]*'0'
				flag += const_seq1[k]*'1'
			res = long_to_bytes(int(flag,2))
			if b'shellmates{' in res:
				print(res.decode())
				break

