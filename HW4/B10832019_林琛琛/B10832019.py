import random
import sys
import base64

# find x^h % n
def Square_and_Multiply(h, x, n):
    h = str(bin(h))[2:]
    y = 1
    for ht in h:
        y = (y * y) % n
        if ht == '1':
            y = (y * x) % n
    return y

# https://www.geeksforgeeks.org/weak-rsa-decryption-chinese-remainder-theorem/
def CRT(p, q, d, y):
    dp = d % (p - 1)
    dq = d % (q - 1)
    m1 = Square_and_Multiply(dp, y, p)
    m2 = Square_and_Multiply(dq, y, q)
    qinv = modinv(q, p)
    h = (qinv * (m1 - m2)) % p
    m = m2 + h * q
    return m
    
# check n is a prime or not
def Miller_Rabin_Test(n):
    if n % 2 == 0:
        return False
    
    m = n - 1 # when k = 0, then N-1 = 2^0 * m -> m = N - 1
    k = 0
    while m % 2 == 1:
        m = m / 2
        k = k + 1
    
    a = random.randint(2, n-2)
    b = Square_and_Multiply(m, a, n) # b = a^m % n
    if b != 1 and b != n-1:
        i = 1
        while i < k and b != n-1:
            b = Square_and_Multiply(2, b, n) # b = b^2 % n
            if b == 1:
                return False
            i = i + 1
        if b != n-1:
            return False
    return True

# get a random prime number with length n
def get_prime(n):
    p =  random.randint(2**n, 2**(n+1))
    while Miller_Rabin_Test(p) == False:
        p = random.randint(2**n, 2**(n+1))
    return p

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

# find the smallest valid e
def get_e(phi):
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            return i

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def encrypt(plaintext, n, e):
    temp = ""
    for c in plaintext:
        temp += str(ord(c) + 100)
    ciphertext = Square_and_Multiply(e, int(temp), n)
    message_bytes = str(ciphertext).encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def decrypt(ciphertext, n, d):
    ciphertext = ciphertext.encode('ascii')
    ciphertext = base64.b64decode(ciphertext)
    ciphertext = int(ciphertext.decode('ascii'))
    plaintext = ""
    temp = str(Square_and_Multiply(d, int(ciphertext), n))
    for i in range(0, len(temp), 3):
        plaintext += chr(int(temp[i:i+3]) - 100)
    return plaintext

def CRT_decrypt(ciphertext, p, q, d):
    ciphertext = ciphertext.encode('ascii')
    ciphertext = base64.b64decode(ciphertext)
    ciphertext = int(ciphertext.decode('ascii'))
    plaintext = ""
    temp = str(CRT(p, q, d, ciphertext)) # 用 CRT 來decode
    for i in range(0, len(temp), 3):
        plaintext += chr(int(temp[i:i+3]) - 100)
    return plaintext

if __name__ == '__main__':
    key_size = 1024

    if sys.argv[1] == '-i':
        p = get_prime(key_size)
        q = get_prime(key_size)
        n = p * q
        phi_n = (p - 1) * (q - 1)
        e = get_e(phi_n)
        d = modinv(e, phi_n)

        print('p =', p)
        print('q =', q)
        print('N =', n)
        print('phi =', phi_n)
        print('e =', e)
        print('d =', d)
    elif sys.argv[1] == '-e':
        msg = sys.argv[2]
        n = int(sys.argv[3])
        e = int(sys.argv[4])

        ciphertext = encrypt(msg, n, e)
        print(ciphertext)

    elif sys.argv[1] == '-d':
        msg = sys.argv[2]
        n = int(sys.argv[3])
        d = int(sys.argv[4])

        plaintext = decrypt(msg, n, d)
        print(plaintext)

    elif sys.argv[1] == '-CRT':
        msg = sys.argv[2]
        p = int(sys.argv[3])
        q = int(sys.argv[4])
        d = int(sys.argv[5])

        plaintext = CRT_decrypt(msg, p, q, d)
        print(plaintext)

# online tools: (檢查用)
# https://www.calculator.net/big-number-calculator.html
# https://www.numberempire.com/primenumbers.php
# https://www.base64encode.org/