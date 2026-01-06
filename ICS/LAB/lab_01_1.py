# Caesar Cipher Algorithm Implementation

# 1. Substitution Method - Replace each letter with the 3rd letter in the alphabet
# 2. Cipher Key - 3
# 3. Encryption - Encrypt the plaintext message using the cipher key
# 4. Decryption - Decrypt the encrypted message using the cipher key

def caesar_cipher_encryption(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            n = key % 26  # Normalize key to 0-25
            if char.islower():
                x = ord(char) - ord('a')  # Convert letter to position (0-25)
                E_n = (x + n) % 26  # Encryption formula: E_n(x) = (x+n) mod 26
                encrypted_message += chr(E_n + ord('a'))  # Convert back to character
            else:
                x = ord(char) - ord('A')  # Convert letter to position (0-25)
                E_n = (x + n) % 26  # Encryption formula: E_n(x) = (x+n) mod 26
                encrypted_message += chr(E_n + ord('A'))  # Convert back to character
        else:
            encrypted_message += char
    return encrypted_message


def caesar_cipher_decryption(message, key):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            n = key % 26  # Normalize key to 0-25
            if char.islower():
                x = ord(char) - ord('a')  # Convert letter to position (0-25)
                D_n = (x - n) % 26  # Decryption formula: D_n(x) = (x-n) mod 26
                decrypted_message += chr(D_n + ord('a'))  # Convert back to character
            else:
                x = ord(char) - ord('A')  # Convert letter to position (0-25)
                D_n = (x - n) % 26  # Decryption formula: D_n(x) = (x-n) mod 26
                decrypted_message += chr(D_n + ord('A'))  # Convert back to character
        else:
            decrypted_message += char
    return decrypted_message



user_input = input("Do You Wish To Encrypt Or Decrypt (Enter 0 for encrypt, 1 for decrypt): ")
if user_input == "0":
    user_input = input("Enter a message to encrypt: ")
    encrypted_message = caesar_cipher_encryption(user_input, 3)
    print(f"Encrypted message: {encrypted_message}")
elif user_input == "1":
    user_input = input("Enter a message to decrypt: ")
    decrypted_message = caesar_cipher_decryption(user_input, 3)
    print(f"Decrypted message: {decrypted_message}")
else:
    print("Invalid input")