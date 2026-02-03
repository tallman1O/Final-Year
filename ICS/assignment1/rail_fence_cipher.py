def rail_fence_encrypt(text: str, rails: int) -> str:
    if rails <= 1 or rails >= len(text):
        return text

    fence = [[] for _ in range(rails)]
    row = 0
    direction = 1

    for ch in text:
        fence[row].append(ch)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return ''.join(''.join(r) for r in fence)


def rail_fence_decrypt(cipher: str, rails: int) -> str:
	"""Decrypt `cipher` produced by the Rail Fence cipher.
	Works for any ASCII characters and returns the original text.
	"""
	if rails <= 1 or rails >= len(cipher):
		return cipher

	rail_lengths = [0] * rails
	row = 0
	direction = 1
	for _ in range(len(cipher)):
		rail_lengths[row] += 1
		row += direction
		if row == 0 or row == rails - 1:
			direction *= -1

	rails_list = []
	idx = 0
	for length in rail_lengths:
		rails_list.append(list(cipher[idx:idx + length]))
		idx += length

	result_chars = []
	row = 0
	direction = 1
	for _ in range(len(cipher)):
		result_chars.append(rails_list[row].pop(0))
		row += direction
		if row == 0 or row == rails - 1:
			direction *= -1

	return ''.join(result_chars)

selection = int(input("Rail Fence Cipher Encryption/Decryption\n 1. Encrypt a word\n 2. Decrypt a word\n"))
if selection == 1:
    word = input("Enter a word to encrypt: ")
    rails = int(input("Enter number of rails: "))
    
    encrypted_word = rail_fence_encrypt(word, rails)
    print("Original word:", word)
    print("Encrypted word:", encrypted_word)
elif selection == 2:
    word = input("Enter a word to decrypt: ")
    rails = int(input("Enter number of rails: "))
    
    decrypted_word = rail_fence_decrypt(word, rails)
    print("Encrypted word:", word)
    print("Decrypted word:", decrypted_word)
else:
    print("Invalid selection. Please choose 1 or 2.")


