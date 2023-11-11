from flask import Flask, render_template, request, json
from api_scrape.get_titles import get_titles
from api_scrape.get_description import get_descriptions

app = Flask(__name__)

with open("config.json") as config_file:
    config = json.load(config_file)

api_key = config.get("CUSTOM_SEARCH_API_KEY")
cse_id = config.get("CUSTOM_SEARCH_CSE_ID")
keyword_content = None

@app.route('/', methods=['POST', 'GET'])
def index():
    global keyword_content

    if request.method == 'POST':
        keyword_content = request.form['keyword']
        titles = get_titles(api_key, cse_id, keyword_content)
        descriptions = get_descriptions(api_key, cse_id, keyword_content)

        # Combine titles and descriptions into a formatted string
        result = ""
        for title, description in zip(titles, descriptions):
            result += f"Title: {title}\nDescription: {description}\n\n"

        # Return the result as plain text
        return result, 200, {'Content-Type': 'text/plain'}
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
