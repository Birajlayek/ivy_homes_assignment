from collections import deque
import string
from src.api_client import APIClient
import time

class NameExtractor:
    def __init__(self, api_client):
        self.api_client = api_client
        self.names = set()
        self.max_depth = 10

    def extract_names(self):
        queue = deque([""])
        while queue:
            query = queue.popleft()
            if len(query) > self.max_depth:
                continue
            
            try:
                data = self.api_client.get_autocomplete(query)
                if data and 'results' in data:
                    for result in data['results']:
                        if len(result) > 1 and result.isalpha():
                            self.names.add(result)
                        for char in string.ascii_lowercase:
                            queue.append(result + char)
            except Exception as e:
                print(f"Error processing query {query}: {e}")
            
            # Handle rate limiting
            time.sleep(1)
        
        return self.names

if __name__ == "__main__":
    api_client = APIClient("http://35.200.185.69:8000")
    extractor = NameExtractor(api_client)
    names = extractor.extract_names()
    print(f"Extracted Names: {len(names)}")
    print(names)
