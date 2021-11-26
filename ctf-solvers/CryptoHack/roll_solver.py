#!/usr/bin/env python3
from Crypto.Util.number import getPrime, inverse, isPrime, getStrongPrime
from pwn import *
from json import dumps, loads
import random

# binomial expansion
# check https://hgarrereyn.gitbooks.io/th3g3ntl3man-ctf-writeups/content/2017/ASIS_CTF_Quals_2017/problems/DLP/DLP.html
# or Pascal Paillier

conn = remote("socket.cryptohack.org",13403)

q = int(conn.recvline().strip().decode().split(" ")[-1][1:-1], 16)
N = q**2
g = q+1
assert pow(g, q, N) == 1

data = {"g": hex(g), "n": hex(N)}
conn.recvuntil("pow(g,q,n) = 1: ")
conn.sendline(dumps(data))

h = int(conn.recvline().strip().decode().split(" ")[-1][1:-1], 16)
x = (h - 1)//q
assert pow(g, x, N) == h

data = {"x": hex(x)}
conn.recvuntil("What is my private key: ")
conn.sendline(dumps(data))

print(conn.recvline())