'''
simplified AES implementation
encryption: 
1. take input plaintext and key (both 16 bits)
2. generate two round keys from the key
3. initial round: add round key 1 to plaintext
4. round 1:
   a. substitute nibbles using S-box
   b. shift rows
   c. mix columns
   d. add round key 2
5. round 2:
   a. substitute nibbles using S-box
   b. shift rows
   c. add round key 3   
6. output ciphertext

decryption:
1. take input ciphertext and key (both 16 bits)
2. generate two round keys from the key
3. initial round: add round key 3 to ciphertext
4. round 1:
   a. inverse shift rows
   b. inverse substitute nibbles using inverse S-box    
   c. add round key 2
5. round 2:
   a. inverse mix columns
   b. inverse shift rows
   c. inverse substitute nibbles using inverse S-box
   d. add round key 1
6. output plaintext

ouput the values after every round in a formatted manner
'''

# ================== S-AES CONSTANTS ==================

S_BOX = {
    0x0:0x9, 0x1:0x4, 0x2:0xA, 0x3:0xB,
    0x4:0xD, 0x5:0x1, 0x6:0x8, 0x7:0x5,
    0x8:0x6, 0x9:0x2, 0xA:0x0, 0xB:0x3,
    0xC:0xC, 0xD:0xE, 0xE:0xF, 0xF:0x7
}

INV_S_BOX = {v:k for k,v in S_BOX.items()}

RCON1 = 0x80
RCON2 = 0x30

# ================== HELPER FUNCTIONS ==================

def print_state(label, state):
    print(f"{label}:")
    print(f"{state[0][0]:X} {state[0][1]:X}")
    print(f"{state[1][0]:X} {state[1][1]:X}\n")

def to_state(val):
    return [
        [(val >> 12) & 0xF, (val >> 8) & 0xF],
        [(val >> 4) & 0xF, val & 0xF]
    ]

def from_state(state):
    return (
        (state[0][0] << 12) |
        (state[0][1] << 8)  |
        (state[1][0] << 4)  |
        state[1][1]
    )

def add_round_key(state, key):
    k = to_state(key)
    return [[state[i][j] ^ k[i][j] for j in range(2)] for i in range(2)]

# ================== KEY EXPANSION ==================

def g(word, rcon):
    return (
        (S_BOX[word & 0xF] << 4 |
         S_BOX[(word >> 4) & 0xF]) ^ rcon
    )

def key_expansion(key):
    w0 = (key >> 8) & 0xFF
    w1 = key & 0xFF

    w2 = w0 ^ g(w1, RCON1)
    w3 = w2 ^ w1
    w4 = w2 ^ g(w3, RCON2)
    w5 = w4 ^ w3

    k1 = (w0 << 8) | w1
    k2 = (w2 << 8) | w3
    k3 = (w4 << 8) | w5
    return k1, k2, k3

# ================== ROUND OPERATIONS ==================

def sub_nibbles(state):
    return [[S_BOX[x] for x in row] for row in state]

def inv_sub_nibbles(state):
    return [[INV_S_BOX[x] for x in row] for row in state]

def shift_rows(state):
    return [state[0], [state[1][1], state[1][0]]]

def inv_shift_rows(state):
    return shift_rows(state)

def gf_mul(a, b):
    p = 0
    for _ in range(4):
        if b & 1:
            p ^= a
        carry = a & 0x8
        a <<= 1
        if carry:
            a ^= 0x13
        b >>= 1
    return p & 0xF

def mix_columns(state):
    return [
        [
            state[0][0] ^ gf_mul(4, state[1][0]),
            state[0][1] ^ gf_mul(4, state[1][1])
        ],
        [
            gf_mul(4, state[0][0]) ^ state[1][0],
            gf_mul(4, state[0][1]) ^ state[1][1]
        ]
    ]

def inv_mix_columns(state):
    return [
        [
            gf_mul(9, state[0][0]) ^ gf_mul(2, state[1][0]),
            gf_mul(9, state[0][1]) ^ gf_mul(2, state[1][1])
        ],
        [
            gf_mul(2, state[0][0]) ^ gf_mul(9, state[1][0]),
            gf_mul(2, state[0][1]) ^ gf_mul(9, state[1][1])
        ]
    ]

# ================== ENCRYPTION ==================

def encrypt(plaintext, key):
    k1, k2, k3 = key_expansion(key)

    state = to_state(plaintext)
    print_state("Plaintext", state)

    state = add_round_key(state, k1)
    print_state("After AddRoundKey (K1)", state)

    state = sub_nibbles(state)
    print_state("After SubNibbles", state)

    state = shift_rows(state)
    print_state("After ShiftRows", state)

    state = mix_columns(state)
    print_state("After MixColumns", state)

    state = add_round_key(state, k2)
    print_state("After AddRoundKey (K2)", state)

    state = sub_nibbles(state)
    print_state("After SubNibbles", state)

    state = shift_rows(state)
    print_state("After ShiftRows", state)

    state = add_round_key(state, k3)
    print_state("Ciphertext", state)

    return from_state(state)

# ================== DECRYPTION ==================

def decrypt(ciphertext, key):
    k1, k2, k3 = key_expansion(key)

    state = to_state(ciphertext)
    print_state("Ciphertext", state)

    state = add_round_key(state, k3)
    print_state("After AddRoundKey (K3)", state)

    state = inv_shift_rows(state)
    print_state("After InvShiftRows", state)

    state = inv_sub_nibbles(state)
    print_state("After InvSubNibbles", state)

    state = add_round_key(state, k2)
    print_state("After AddRoundKey (K2)", state)

    state = inv_mix_columns(state)
    print_state("After InvMixColumns", state)

    state = inv_shift_rows(state)
    print_state("After InvShiftRows", state)

    state = inv_sub_nibbles(state)
    print_state("After InvSubNibbles", state)

    state = add_round_key(state, k1)
    print_state("Recovered Plaintext", state)

    return from_state(state)

# ================== SAMPLE RUN ==================

if __name__ == "__main__":
    pt = 0x1234
    key = 0x5678

    ct = encrypt(pt, key)
    print(f"Final Ciphertext: {ct:04X}\n")

    recovered = decrypt(ct, key)
    print(f"Final Plaintext: {recovered:04X}")