import unittest
import os
from key_management.key_manager import add_key, get_key

class TestKeyManagement(unittest.TestCase):
    def test_add_get_key(self):
        key_id = "test_key"
        key = "test_key_value"
        add_key(key_id, key.encode())
        retrieved_key = get_key(key_id)
        self.assertEqual(key, retrieved_key)

    def tearDown(self):
        if os.path.exists("keys.json"):
            os.remove("keys.json")

if __name__ == "__main__":
    unittest.main()
