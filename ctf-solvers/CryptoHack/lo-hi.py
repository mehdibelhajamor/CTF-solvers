from pwn import *
import json
from sympy import invert

mod = 2**61 - 1

cards = ["Ace of Clubs","Two of Clubs","Three of Clubs","Four of Clubs","Five of Clubs","Six of Clubs","Seven of Clubs","Eight of Clubs","Nine of Clubs","Ten of Clubs","Jack of Clubs","Queen of Clubs","King of Clubs","Ace of Hearts","Two of Hearts","Three of Hearts","Four of Hearts","Five of Hearts","Six of Hearts","Seven of Hearts","Eight of Hearts","Nine of Hearts","Ten of Hearts","Jack of Hearts","Queen of Hearts","King of Hearts","Ace of Diamonds","Two of Diamonds","Three of Diamonds","Four of Diamonds","Five of Diamonds","Six of Diamonds","Seven of Diamonds","Eight of Diamonds","Nine of Diamonds","Ten of Diamonds","Jack of Diamonds","Queen of Diamonds","King of Diamonds","Ace of Spades","Two of Spades","Three of Spades","Four of Spades","Five of Spades","Six of Spades","Seven of Spades","Eight of Spades","Nine of Spades","Ten of Spades","Jack of Spades","Queen of Spades","King of Spades"]
VALUES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
rand = []
k = [100]*11
conn = remote("socket.cryptohack.org", 13383)

def get_a(values, m):
    s1 = values[-3]
    s2 = values[-2]
    s3 = values[-1]
    return (s3-s2)*int(invert(s2-s1, m)) % m

def get_c(s2, a, s1, m):
    return (s2 - (a*s1)) % m

def rebase(n, b=52):
    if n < b:
        return [n]
    else:
        return [n % b] + rebase(n//b, b)

comp = 0
hand = None
while 1:
    msg = json.loads(conn.recvline())
    hand = msg["hand"]
    index = cards.index(hand)
    k[comp] = index
    comp += 1
    if (100 not in k) and (comp%11 == 0):
        p = k[0]
        s = []
        s.append(p)
        for i in range(len(k)-1):
            p *= 52
            for j in range(52):
                r = (p + j)
                if (r//52 == s[-1]) and (r%52 == k[i+1]) :
                    p = r
                    s.append(p)
                    break
        rand.append(s[-1])
        if len(rand) == 3:
            print("[+] values founded : ",rand)
            break
        k = [100]*11
        comp = 0
    c = random.choice(["l","h"])
    choix = str({"choice" : str(c)}).replace("'",'"')
    conn.sendline(choix)

a = get_a(rand, mod)
b = get_c(rand[-1], a, rand[-2], mod)

print(a)
print(b)
while 1:
    n = (rand[-1]*a + b) % mod
    rand.append(n)
    deals = rebase(n)[::-1]
    for d in deals:
        hidden = cards[d]
        c = None
        hand_value = hand.split(' ')[0]
        hidden_value = hidden.split(' ')[0]
        if VALUES.index(str(hand_value)) < VALUES.index(str(hidden_value)) :
            c = 'higher'
        else :
            c = 'lower'
        choix = str({"choice" : str(c)}).replace("'",'"')
        conn.sendline(choix)
        msg = json.loads(conn.recvline())
        print(msg["msg"])
        hand = msg["hand"]

