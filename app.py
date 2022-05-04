from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content="Testing")

def getNews():
    api_key = "3ca69fda5fa74125b35d01d178d09d42"
    url = "https://newsapi.org/v2/top-headlines?country=us&apikey=" +api_key
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news =""

    for article in articles:
        my_articles.append(article["title"])

    



if __name__ == "__main__":
    app.run(debug=True)