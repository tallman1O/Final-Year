def caesar_cipher_ascii(text, shift):
    """
    Encrypt/decrypt text using Caesar cipher with ASCII values.
    Handles uppercase, lowercase, numbers, and special characters.
    """
    encrypted_text = ""
    
    for char in text:
        ascii_value = ord(char)  
        
        if 65 <= ascii_value <= 90:
            new_value = ((ascii_value - 65 + shift) % 26) + 65
            encrypted_text += chr(new_value)
        
        elif 97 <= ascii_value <= 122:
            new_value = ((ascii_value - 97 + shift) % 26) + 97
            encrypted_text += chr(new_value)
        
        elif 48 <= ascii_value <= 57:
            new_value = ((ascii_value - 48 + shift) % 10) + 48
            encrypted_text += chr(new_value)
        
        else:
            encrypted_text += char
    
    return encrypted_text


selection = int(input("Caesar Cipher ASCII Encryption/Decryption\n 1. Encrpt a word\n 2. Decrypt a word\n"))

if selection == 1:
    word = input("Enter a word to encrypt: ")
    shift = int(input("Enter shift value: "))
    
    encrypted_word = caesar_cipher_ascii(word, shift)
    print("Original word:", word)
    print("Encrypted word:", encrypted_word)
elif selection == 2:
    word = input("Enter a word to decrypt: ")
    shift = int(input("Enter shift value: "))
    
    decrypted_word = caesar_cipher_ascii(word, -shift)
    print("Encrypted word:", word)
    print("Decrypted word:", decrypted_word)
else:
    print("Invalid selection. Please choose 1 or 2.")

