from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route("/")
def hello_world():
    name = "World Wide Web"
    return f"<p>Hello, {name}!!</p>"
