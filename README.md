# Autocomplete API Explorer

This project explores and extracts names from an autocomplete API.

## Approach

1. **Exploration**: Test the API with different queries to understand its behavior.
2. **Name Extraction**: Use a BFS approach to extract all possible names.
3. **Rate Limiting**: Handle rate limiting by introducing delays between requests.

## Findings

- The API returns a list of suggestions for each query.
- Rate limiting is handled by introducing a delay between requests.

## Usage

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the explorer script using `python scripts/explore_api.py`.
4. Extract names using `python src/name_extractor.py`.

## Submission

1. **Code Solution**: The complete codebase.
2. **README**: Explaining the approach and findings.
3. **Tools/Scripts**: Any additional scripts used for testing or exploration.
4. **Total Requests**: The total number of requests made to the API.
5. **Total Records**: The total number of records extracted from the API.
