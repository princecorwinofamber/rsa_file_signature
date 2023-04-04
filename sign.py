import random
import secrets
import hashlib
import math

def random_bytes(count):
    try:
        return secrets.token_bytes(count)
    except:
        return bytes([random.randint(0, 255) for _ in range(count)])

def random_padding(data, block_size):
    if len(data) % block_size != 0:
        padding = random_bytes(len(data) % block_size)
        return data + padding
    else:
        return data

def pow_mod(num, pow, mod):
    result = 1
    while pow > 0:
        if pow % 2 == 0:
            num = num ** 2 % mod
            pow //= 2
        else:
            result = (result * num) % mod
            pow -= 1
    return result

def encrypt(data, private_key):
    e, n = private_key
    return pow_mod(data, e, n)

def decrypt(data, public_key):
    d, n = public_key
    return pow_mod(data, d, n)

def sign(data, private_key):
    sha1 = int.from_bytes(hashlib.sha1(data).digest(), "big", signed=False) % private_key[1]
    return encrypt(sha1, private_key)

def verify(data, signature, public_key):
    sha1 = int.from_bytes(hashlib.sha1(data).digest(), "big", signed=False) % public_key[1]
    return sha1 == decrypt(signature, public_key)

filename = input("Please, enter the name of the file to sign: ")
private_key = tuple(map(int, input("Please, enter the private key: ").replace(" ", "").split(",")))
f = open(filename, "rb")
signature = sign(f.read(), private_key)
f.close()
f = open(filename + ".signature", "w")
f.write(str(signature))
f.close()
print("Signature written to file {}".format(filename + ".signature"))
