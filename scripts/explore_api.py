from src.api_client import APIClient

def explore_api():
    api_client = APIClient("http://35.200.185.69:8000")
    
    # Test with different queries
    queries = ["a", "ab", "abc"]
    for query in queries:
        print(f"Query: {query}")
        print(api_client.get_autocomplete(query))

if __name__ == "__main__":
    explore_api()
