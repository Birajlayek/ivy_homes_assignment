import unittest
from src.api_client import APIClient

class TestAPIClient(unittest.TestCase):
    def test_get_autocomplete(self):
        api_client = APIClient("http://35.200.185.69:8000")
        response = api_client.get_autocomplete("a")
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
