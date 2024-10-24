from wsgiref.util import application_uri
from flask import Flask
app = Flask(application_uri)

@app.route("C:User/dus08/OneDrive/Documents/Github/AutoGPT/autogpt_platform/autogpt_libs/pyproject.toml")
def hello():
    return "Hello World!"
