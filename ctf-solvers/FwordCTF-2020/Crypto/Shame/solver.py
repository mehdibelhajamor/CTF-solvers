
#FwordCTF{shame_on_shamir_he_deserves_walk_of_shame}
#secret=564321784322132454256546212165454321321
k=0x4

#f(x)=S+A*x+B*x^2+C*x^3

#Solver : 
A=564321784322132454256546212165481243585
B=564321784322132454256546212165579958807
C=564321784322132454256546212165804306769
Max=C+A-2*B #will be explained!
i=0
t=[]
print (Max)
print (len(str(Max)))

while (Max-2*i >=0):
	if (Max-2*i)%12 == 0:
		t.append((Max-2*i)/12)
	i+=1
searching=3*A+C-3*B
possible_secret=[]
w=open('wordlist.txt','w+')	
for i in t:
	if (searching-6*i)>=0:
		w.write(str(searching-6*i)+'\n')

#then bruteforce the password using fcrackzip!
