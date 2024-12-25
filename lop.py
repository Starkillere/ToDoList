import hashlib

def generate_password_hash(password: str) -> str:
    """
    Generate a SHA-256 hash for a given password.

    Args:
        password (str): The plaintext password to hash.

    Returns:
        str: The SHA-256 hash of the password.
    """
    # Encode the password to bytes, then hash it using SHA-256
    hash_object = hashlib.sha256(password.encode())
    password_hash = hash_object.hexdigest()
    return password_hash

if __name__ == "__main__":
    # Prompt the user to enter their password
    password = input("Enter the password to hash: ")
    hashed_password = generate_password_hash(password)
    print(f"SHA-256 Hash: {hashed_password}")
