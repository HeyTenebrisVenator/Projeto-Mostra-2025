from flask import Flask, send_file, request, jsonify
import Complete
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_file("Site/home.html")

@app.route("/url")
def url():
    return send_file("Site/url.html")

@app.route("/title")
def title():
    return send_file("Site/title.html")

@app.route("/check")
def escolha():
    return send_file("Site/escolha.html")

@app.route("/script.js")
def js():
    return send_file("Site/script.js")

# URL
@app.route("/send_url")
def send_url():
    arg = request.args.get("data")
    print(arg)
    return Complete.url(arg)

# TITLE
@app.route("/send_title")
def send_title():
    arg = request.args.get("data")
    return Complete.body(arg)

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
