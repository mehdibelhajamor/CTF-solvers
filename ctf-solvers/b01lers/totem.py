# You can install these packages to help w/ solving unless you have others in mind
# i.e. python3 -m pip install {name of package}
from pwn import *
import codecs
from base64 import b64decode
from string import ascii_lowercase

HOST = 'chal.ctf.b01lers.com'
PORT = 2008

r = remote(HOST,PORT)

lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab', 
        'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba', 
        'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb', 
        'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}

def bacon(s):
    message = s.lower()
    decipher = '' 
    i = 0
    while True : 
        if(i < len(message)-4): 
            substr = message[i:i + 5] 
            if(substr[0] != ' '): 
                decipher += list(lookup.keys())[list(lookup.values()).index(substr)] 
                i += 5
            else: 
                decipher += ' '
                i += 1
        else: 
            break
    return decipher.lower()

lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V', 
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q', 
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G', 
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'} 

def rot13(s):
    return codecs.decode(s, 'rot_13')

def atbash(s):
    cipher = '' 
    for letter in s: 
        if (letter != ' '): 
            cipher += lookup_table[letter.upper()].lower() 
        else: 
            cipher += ' '
    return cipher

def Base64(s):
    return b64decode(s)

if __name__ == '__main__':
    count = 0
    while True:     
        r.recvuntil('Method: ')
        method = r.recvuntil('\n').strip()
        r.recvuntil('Ciphertext: ')
        argument = r.recvuntil('\n').strip()

        result = globals()[method.decode()](argument.decode())  # :)

        r.recv()
        r.sendline(result)
        count += 1
        print(count)
        if count == 1000:
            print(r.recv())
            exit(0)
    
