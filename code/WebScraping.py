#!C:\Users\T C\AppData\Local\Programs\Python\Python311\python.exe
print("Content-type: text/html\n\n")
import cgi
import requests

# Set your API key and Custom Search Engine ID
api_key = "API KEY of Custom Search Engine "
cse_id = "Custom Search Engine ID"

form = cgi.FieldStorage()

if "keyword" in form:
    keyword = form.getvalue("keyword")

# Construct the URL for the Custom Search API
url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={keyword}"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    if 'items' in data:
        search_results = data['items']

        for i, result in enumerate(search_results[:10]):
            title = result['title']
            description = result.get('snippet', '')

            print(f"Result {i + 1} - Title: {title}")
            print(f"Description: {description}")
            print()

    else:
        print("No search results found.")
else:
    print("Failed to retrieve Google search results. Status Code:", response.status_code)
