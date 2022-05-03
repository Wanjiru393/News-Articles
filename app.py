from flask import Flask, render_template
# from newsapi import NewsApiClient

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")


# @app.route("/")
# def index():
#     newsapi = NewsApiClient(api_key="3ca69fda5fa74125b35d01d178d09d42")



if __name__ == "__main__":
    app.run()