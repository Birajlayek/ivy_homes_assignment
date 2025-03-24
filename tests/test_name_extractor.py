import unittest
from src.name_extractor import NameExtractor
from src.api_client import APIClient

class TestNameExtractor(unittest.TestCase):
    def test_extract_names(self):
        api_client = APIClient("http://35.200.185.69:8000")
        extractor = NameExtractor(api_client)
        names = extractor.extract_names()
        self.assertIsInstance(names, set)

if __name__ == '__main__':
    unittest.main()
