import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from api_client import APIClient

def explore_api():
    api_client = APIClient("http://35.200.185.69:8000")
    
    # Test with different queries
    queries = ["a", "ab", "abc"]
    for query in queries:
        print(f"Query: {query}")
        print(api_client.get_autocomplete(query))

explore_api()
