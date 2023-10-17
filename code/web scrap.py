import requests
from bs4 import BeautifulSoup

def google_search_scraper(keyword):
    url = f"https://www.google.com/search?q={keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract and process the search results here
        # You can parse the HTML to retrieve information from the top 10 results.
        # Extract titles, URLs, and descriptions.

        # Example: Extracting and printing the titles of the search results
        results = soup.find_all('h3')
        for result in results:
            print(result.get_text())
    else:
        print("Failed to retrieve search results")

if __name__ == '__main__':
    keyword = input("Enter a keyword: ")
    google_search_scraper(keyword)
