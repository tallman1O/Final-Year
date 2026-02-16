'''
import hashlib
input1 = input("Enter text/image: ")
hash_object = hashlib.md5(input1.encode())
print(hash_object.hexdigest())
take input of new text/image and print the hash value of it as well
compare both hash values 
print data is tampered/ data not tampered based on the comparison
take input choice to use md5 algorithm or sha256 algorithm
'''

import hashlib
import os


def compute_hash(input_value: str, algorithm: str = "md5") -> str:
    if os.path.isfile(input_value):
        with open(input_value, "rb") as f:
            data = f.read()
    else:
        data = input_value.encode()

    alg = algorithm.lower()
    if alg == "md5":
        h = hashlib.md5()
    elif alg == "sha256":
        h = hashlib.sha256()
    else:
        raise ValueError("Unsupported algorithm")

    h.update(data)
    return h.hexdigest()


def choose_algorithm() -> str:
    while True:
        choice = input("Choose algorithm ('md5' or 'sha256') [md5]: ").strip().lower()
        if choice == "":
            return "md5"
        if choice in ("md5", "sha256"):
            return choice
        print("Invalid choice. Enter 'md5' or 'sha256'.")


def main() -> None:
    alg = choose_algorithm()

    original = input("Enter text or file path for original data: ")
    hash1 = compute_hash(original, alg)
    print(f"{alg} hash: {hash1}")

    new = input("Enter text or file path for new data: ")
    hash2 = compute_hash(new, alg)
    print(f"{alg} hash: {hash2}")

    if hash1 == hash2:
        print("Data is not tampered")
    else:
        print("Data is tampered")


if __name__ == "__main__":
    main()