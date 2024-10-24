from flask import Flask
app = Flask(1.1.2)

@app.route("/")
def hello():
    return "Hello World!"
