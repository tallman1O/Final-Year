import hashlib

# -----------------------------
# Helper Functions
# -----------------------------

def xor_bits(a, b):
    """XOR two binary strings of equal length"""
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))


def string_to_bin(text):
    """Convert string to binary"""
    return ''.join(format(ord(c), '08b') for c in text)


def bin_to_string(binary):
    """Convert binary to string"""
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)


# -----------------------------
# Round Function F
# -----------------------------

def round_function(right, key):
    """
    Simple round function:
    Hash(right + key) → take required number of bits
    """
    data = right + key
    hashed = hashlib.sha256(data.encode()).hexdigest()
    hashed_bin = bin(int(hashed, 16))[2:].zfill(256)

    return hashed_bin[:len(right)]  # Match right half size


# -----------------------------
# Feistel Encrypt
# -----------------------------

def feistel_encrypt(plaintext, keys, rounds=4):
    binary = string_to_bin(plaintext)

    # Ensure even length
    if len(binary) % 2 != 0:
        binary += '0'

    left = binary[:len(binary)//2]
    right = binary[len(binary)//2:]

    for i in range(rounds):
        temp = right
        f_output = round_function(right, keys[i])
        right = xor_bits(left, f_output)
        left = temp

    return left + right


# -----------------------------
# Feistel Decrypt
# -----------------------------

def feistel_decrypt(cipher_bin, keys, rounds=4):
    left = cipher_bin[:len(cipher_bin)//2]
    right = cipher_bin[len(cipher_bin)//2:]

    for i in reversed(range(rounds)):
        temp = left
        f_output = round_function(left, keys[i])
        left = xor_bits(right, f_output)
        right = temp

    decrypted_bin = left + right
    return bin_to_string(decrypted_bin)


# -----------------------------
# Example Usage
# -----------------------------

if __name__ == "__main__":
    plaintext = "HELLO"
    round_keys = ["K1", "K2", "K3", "K4"]

    print("Plaintext:", plaintext)

    cipher = feistel_encrypt(plaintext, round_keys)
    print("Encrypted (binary):", cipher)

    decrypted = feistel_decrypt(cipher, round_keys)
    print("Decrypted:", decrypted)
