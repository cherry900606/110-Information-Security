from random import randint
import random
from sys import argv


def squre_and_multiply(x, h, n):
    h = str(bin(h))[2:] # 去除 "0b"
    res = 1
    for i in h: # see through each bit
        res = (res * res) % n
        if i == '1':
            res = (res * x) % n
    return res

# not using, just a slow prime number test method
def fermat_test(p, s = 10):
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    
    for i in range (1, s):
        print(i)
        r = randint(1, p - 1)
        if pow(r, p-1) % p != 1:
            return False
    return True


# a faster prime number test method
def miller_rabin_test(n):  
    
    # pre test
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 還原 pow(2, r) == n - 1, get r
    r = 0
    s = n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
        
    for _ in range(0, 10):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(0, r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def gcd(m, n):
    if m == 0:
        return (n, 0, 1)
    else:
        g, y, x = gcd(n % m, m)
        return (g, x - (n // m) * y, y)
    
def get_inverse(m, n):
    g1, x, g2 = gcd(m, n)
    return x % n 

def get_pq():
    length = 1024
    res = randint(pow(2, length), pow(2, length + 1))
    while miller_rabin_test(res) == False:
        res = randint(pow(2, length), pow(2, length + 1))
    return res
        
##################################################
##################################################

#"""
mode = argv[1]
if mode != '-i': 
    sec = int(argv[3][2:], 16)
    thi = int(argv[4][2:], 16)
if mode == '-i': ## print p, q, n, e, d   
   p = get_pq()
   q = get_pq()
   n = p * q
   e = 17
   d = get_inverse(e, (p-1) * (q-1))
   
   print('p = ', hex(p))
   print('q = ', hex(q))
   print('n = ', hex(n))
   print('e = ', hex(e))
   print('d = ', hex(d))   
   
elif mode == '-e': ## encode
    plain = argv[2]
    n, e = sec, thi
    y = ""
    for i in plain:
        ch = ord(i)
        y += hex(squre_and_multiply(ch, e, n))
    print(y)
    
elif mode == '-d': ## decode
    cipher = argv[2].split('0x')
    cipher = cipher[1: ]
    n, d = sec, thi
    y = ""
    for i in cipher:
        i = int(i, 16)
        y += chr(squre_and_multiply(i, d, n))
    print(y)
#"""