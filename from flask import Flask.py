from wsgiref.util import application_uri  # noqa: F401
from flask import Flask # type: ignore
app = Flask(AutoGPT)  # type: ignore # noqa: F821

@app.route("C:User/dus08/OneDrive/Documents/Github/AutoGPT/autogpt_platform/autogpt_libs/pyproject.toml")
def hello():
    return "Hello World!"
