# Rail Fence Cipher Algorithm Implementation

# 1. Rail Fence Method - Arrange the letters in a zigzag pattern
# 2. Cipher Key - 3
# 3. Encryption - Encrypt the plaintext message using the cipher key
# 4. Decryption - Decrypt the encrypted message using the cipher key

def rail_fence_encryption(message, key):
    if key == 1:
        return message

    # Step 1: Remember where spaces are in the original message
    space_positions = []
    for i in range(len(message)):
        if message[i] == ' ':
            space_positions.append(i)
    
    # Step 2: Remove spaces and keep only letters
    letters_only = ""
    for char in message:
        if char != ' ':
            letters_only += char
    
    # Step 3: Create empty rails (rows)
    rails = []
    for i in range(key):
        rails.append("")
    
    # Step 4: Write letters to rails in zigzag pattern
    rail = 0
    direction = 1  # 1 means going down, -1 means going up
    for char in letters_only:
        rails[rail] += char
        rail += direction
        # Change direction when we reach top or bottom rail
        if rail == 0 or rail == key - 1:
            direction = direction * -1
    
    # Step 5: Read all rails from top to bottom
    encrypted_letters = ""
    for i in range(key):
        encrypted_letters += rails[i]
    
    # Step 6: Put spaces back in their original positions
    result = list(encrypted_letters)
    for pos in space_positions:
        if pos <= len(result):
            result.insert(pos, ' ')
    
    return ''.join(result)

def rail_fence_decryption(message, key):
    if key == 1:
        return message

    # Step 1: Remember where spaces are in the encrypted message
    space_positions = []
    for i in range(len(message)):
        if message[i] == ' ':
            space_positions.append(i)
    
    # Step 2: Remove spaces and keep only letters
    letters_only = ""
    for char in message:
        if char != ' ':
            letters_only += char
    
    # Step 3: Figure out how many characters go to each rail
    # We need to simulate the zigzag pattern to count characters per rail
    rail_lengths = []
    for i in range(key):
        rail_lengths.append(0)
    
    rail = 0
    direction = 1
    for i in range(len(letters_only)):
        rail_lengths[rail] += 1
        rail += direction
        if rail == 0 or rail == key - 1:
            direction = direction * -1
    
    # Step 4: Split encrypted message into rails based on lengths
    start = 0
    rails = []
    for i in range(key):
        length = rail_lengths[i]
        rails.append(letters_only[start:start + length])
        start += length
    
    # Step 5: Read characters from rails in zigzag pattern to reconstruct original
    rail_indices = []
    for i in range(key):
        rail_indices.append(0)
    
    decrypted_letters = ""
    rail = 0
    direction = 1
    for i in range(len(letters_only)):
        decrypted_letters += rails[rail][rail_indices[rail]]
        rail_indices[rail] += 1
        rail += direction
        if rail == 0 or rail == key - 1:
            direction = direction * -1
    
    # Step 6: Put spaces back in their original positions
    result = list(decrypted_letters)
    for pos in space_positions:
        if pos <= len(result):
            result.insert(pos, ' ')
    
    return ''.join(result)

def __main__():
    user_input = input("Do You Wish To Encrypt Or Decrypt (Enter 0 for encrypt, 1 for decrypt): ")
    if user_input == "0":
        user_input = input("Enter a message to encrypt: ")
        encrypted_message = rail_fence_encryption(user_input, 3)
        print(f"Encrypted message: {encrypted_message}")
    elif user_input == "1":
        user_input = input("Enter a message to decrypt: ")
        decrypted_message = rail_fence_decryption(user_input, 3)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    __main__()