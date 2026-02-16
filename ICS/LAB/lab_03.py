S  = [9,4,10,11,13,1,8,5,6,2,0,3,12,14,15,7]
Si = [10,5,9,11,1,7,8,15,6,0,2,3,12,4,13,14]
R  = [0x80, 0x30]

# ---- Utilities ----
sub  = lambda x: (S[x>>4]<<4) | S[x&0xF]
isub = lambda x: (Si[x>>4]<<4) | Si[x&0xF]
rot  = lambda x: ((x&0xF)<<4)|(x>>4)
ark  = lambda s,k: s^k

def gf(a,b):
    p=0
    for _ in range(4):
        if b&1: p^=a
        a=(a<<1)^(0b10011 if a&0x8 else 0)
        b>>=1
    return p&0xF

def mix(s,inv=False):
    s0,s1,s2,s3 = s>>12,(s>>8)&15,(s>>4)&15,s&15
    if not inv:
        t=[s0^gf(4,s2), s1^gf(4,s3), s2^gf(4,s0), s3^gf(4,s1)]
    else:
        t=[gf(9,s0)^gf(2,s2), gf(9,s1)^gf(2,s3),
           gf(9,s2)^gf(2,s0), gf(9,s3)^gf(2,s1)]
    return (t[0]<<12)|(t[1]<<8)|(t[2]<<4)|t[3]

shift = lambda s: (s&0xF0F0)|((s&0x0F00)>>8)|((s&0x000F)<<8)

# ---- Key Expansion ----
def expand(k):
    w0,w1 = k>>8, k&0xFF
    w2 = w0 ^ sub(rot(w1)) ^ R[0]
    w3 = w2 ^ w1
    w4 = w2 ^ sub(rot(w3)) ^ R[1]
    w5 = w4 ^ w3
    return (k, (w2<<8)|w3, (w4<<8)|w5)

# ---- Encrypt ----
def encrypt(p,k):
    k0,k1,k2 = expand(k)
    s = ark(p,k0)
    s = shift((sub(s>>8)<<8)|sub(s&0xFF))
    s = ark(mix(s),k1)
    s = shift((sub(s>>8)<<8)|sub(s&0xFF))
    return ark(s,k2)

# ---- Decrypt ----
def decrypt(c,k):
    k0,k1,k2 = expand(k)
    s = ark(c,k2)
    s = (isub(s>>8)<<8)|isub(s&0xFF)
    s = shift(s)
    s = mix(ark(s,k1),True)
    s = (isub(s>>8)<<8)|isub(s&0xFF)
    s = shift(s)
    return ark(s,k0)

# ---- Example ----
if __name__ == "__main__":
    pt  = 0b1101011100101000
    key = 0b0100101011110101

    ct = encrypt(pt,key)
    dt = decrypt(ct,key)

    print("Plain :", format(pt,'016b'))
    print("Cipher:", format(ct,'016b'))
    print("Back  :", format(dt,'016b'))
