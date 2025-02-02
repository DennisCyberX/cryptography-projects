import unittest
from encryption_tool.encrypt_decrypt import generate_key, encrypt_data, decrypt_data

class TestEncryption(unittest.TestCase):
    def test_encrypt_decrypt(self):
        key = generate_key()
        data = "Hello, World!"
        encrypted_data = encrypt_data(data, key)
        decrypted_data = decrypt_data(encrypted_data, key)
        self.assertEqual(data, decrypted_data)

if __name__ == "__main__":
    unittest.main()
