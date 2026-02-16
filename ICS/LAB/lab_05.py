import hashlib

# ---- Generate Hash ----
def generate_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()

# ---- Verify Integrity ----
def verify_message(original_message, received_hash):
    new_hash = generate_hash(original_message)
    return new_hash == received_hash

# ---- Example ----
if __name__ == "__main__":
    message = input("Enter message: ")

    # Sender side
    hash_value = generate_hash(message)
    print("Generated Hash:", hash_value)

    # Receiver side
    received_message = message  # simulate transfer
    received_hash = hash_value

    if verify_message(received_message, received_hash):
        print("Message integrity verified ✔")
    else:
        print("Message altered ✘")
