import os
import json
from cryptography.fernet import Fernet

KEY_FILE = "keys.json"

def load_keys():
    """Load keys from the key file."""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_keys(keys):
    """Save keys to the key file."""
    with open(KEY_FILE, "w") as f:
        json.dump(keys, f)

def add_key(key_id, key):
    """Add a new key to the key management system."""
    keys = load_keys()
    keys[key_id] = key.decode()
    save_keys(keys)

def get_key(key_id):
    """Retrieve a key by its ID."""
    keys = load_keys()
    return keys.get(key_id)

if __name__ == "__main__":
    key_id = input("Enter key ID: ")
    key = Fernet.generate_key()
    add_key(key_id, key)
    print(f"Key added: {key_id}")

    retrieved_key = get_key(key_id)
    print(f"Retrieved Key: {retrieved_key}")
