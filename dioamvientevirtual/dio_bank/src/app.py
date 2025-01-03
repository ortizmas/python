from flask import Flask, url_for, request
import json

app = Flask(__name__)
app.debug = True


@app.route("/")
def hello_world():
    name = "World Wide Web"
    return f"<p>Hello, {name}!!</p>"


@app.route("/user/<username>/<int:old>")
def hello_world_params(username, old):
    name = "Sr."
    print(f"Tipo da variable idade: {type(old)}")
    return f"<p>Hello, {name} {username} (Tipo da variable idade: {old})!!</p>"


@app.route("/about")
def about():
    name = "Sr."
    return f"<p>Hello, {name} Eber!!</p>"


@app.route("/contact")
def contact():
    name = "Contato ."
    return f"<p>Nosso, {name}!!</p>"


@app.route("/projects", methods=["GET", "POST"])
def projects():
    method = request.method
    if method == "POST":
        data = json.loads(request.data.decode("utf-8"))
        return data["cnpj"]
    return f"The project page {method}"


with app.test_request_context():
    print(url_for("contact"))
    print(url_for("about", next="/"))
