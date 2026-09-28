from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Day 6 AWS Flask Deployment is running!"


@app.route("/health")
def health():
    return "OK"
