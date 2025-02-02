import unittest
from digital_signature.signature_system import generate_key_pair, sign_data, verify_signature

class TestSignature(unittest.TestCase):
    def test_sign_verify(self):
        private_key, public_key = generate_key_pair()
        data = "Hello, World!"
        signature = sign_data(data, private_key)
        is_valid = verify_signature(data, signature, public_key)
        self.assertTrue(is_valid)

if __name__ == "__main__":
    unittest.main()
