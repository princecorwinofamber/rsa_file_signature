import random
import secrets
import hashlib
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def is_prime(n, k=40):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime_number(n):
    while True:
        p = random.randint(2**(n-1), 2**n - 1)
        if is_prime(p):
            return p

def generate_key_pair(key_size):
    p = generate_prime_number(key_size // 2)
    q = generate_prime_number(key_size // 2)

    n = p * q
    phi = lcm(p - 1, q - 1)

    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = pow(e, -1, phi)

    # (public key, private key) is returned
    return (e, n), (d, n)

public_key, private_key = generate_key_pair(512)
print("Public key:", str(public_key)[1:-1])
print("Private key:", str(private_key)[1:-1])
