
lines = open("file.txt","r+").readlines()

for j in range(172):
	i = j
	flag = ''
	for line in lines:
		flag += line.strip()[i%172]
		i+=1
	print flag+'\n'
