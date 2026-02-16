import random
from math import gcd

# ---- Extended Euclidean Algorithm ----
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# ---- Key Generation ----
def generate_keys():
    p = 61   # small primes (educational purpose)
    q = 53
    n = p * q
    phi = (p-1)*(q-1)

    e = 17   # must be coprime with phi
    d = modinv(e, phi)

    return (e, n), (d, n)

# ---- Encryption ----
def encrypt(message, pub):
    e, n = pub
    return [pow(ord(ch), e, n) for ch in message]

# ---- Decryption ----
def decrypt(cipher, priv):
    d, n = priv
    return ''.join(chr(pow(c, d, n)) for c in cipher)

# ---- Example ----
if __name__ == "__main__":
    public, private = generate_keys()

    msg = "HELLO"
    cipher = encrypt(msg, public)
    decrypted = decrypt(cipher, private)

    print("Public Key :", public)
    print("Private Key:", private)
    print("Cipher     :", cipher)
    print("Decrypted  :", decrypted)
