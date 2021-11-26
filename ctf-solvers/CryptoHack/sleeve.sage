from sage.all import *
from fastecdsa.curve import P256
from fastecdsa.point import Point
from Crypto.Random import random
from Crypto.Util.number import inverse, long_to_bytes, bytes_to_long
from sage.rings.integer import Integer
from pwn import *
from json import loads, dumps


while 1:
  try:
    conn = remote("socket.cryptohack.org", 13387)
    conn.recvline()

    class RNG:
        def __init__(self, seed, P, Q):
            self.seed = seed
            self.P = P
            self.Q = Q

        def next(self):
            t = self.seed
            s = int((t * self.P)[0])
            self.seed = s
            r = int((s * self.Q)[0])
            return r & (2**(8 * 30) - 1)

    def rebase(n, b=37):
      if n < b:
        return [n]
      else:
        return [n % b] + rebase(n//b, b)

    # Generate Q
    a = P256.a
    b = P256.b
    p = P256.p
    E = EllipticCurve(GF(p), [a, b])
    q = E.order()
    P = E(0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
    d = 123456789
    invd = inverse(d, q)
    Q = invd*P

    x = hex(Q[0])[2:]
    y = hex(Q[1])[2:]
    conn.sendline(dumps({"x": x, "y":y}))
    conn.recvline()

    bet = 30

    # Calculate r1
    tab = []
    for _ in range(46):
      conn.sendline(dumps({"choice": bet}))
      res = loads(conn.recvline())
      print(res["$"])
      spin = int(res['spin'])
      tab.append(spin)
    r1 = int(tab[0])
    for i in range(1, len(tab)):
        r1 = r1*37 + tab[i]

    # Calculate r2
    tab = []
    for _ in range(46):
      conn.sendline(dumps({"choice": bet}))
      res = loads(conn.recvline())
      print(res["$"])
      spin = int(res['spin'])
      tab.append(spin)
    r2 = int(tab[0])
    for i in range(1, len(tab)):
        r2 = r2*37 + tab[i]

    seed = 0
    for i in range(65537):
      x = Integer(bytes_to_long(long_to_bytes(int(i)) + long_to_bytes(r1)))
      try:
        sQ = E.lift_x(x)
        sP = d*sQ
        seed = int(sP[0])
        rec_r = int((seed * Q)[0]) & (2**(8 * 30) - 1)
        if rec_r == r2:
          print("Found seed: ",seed)
          break
      except:
        pass

    rng = RNG(seed, P, Q)
    n = rng.next()
    spins = rebase(n)[::-1]
    print(spins)
    for i in range(len(spins)):
      conn.sendline(dumps({"choice": spins[i]}))
      print(loads(conn.recvline()))
  except:
    pass
