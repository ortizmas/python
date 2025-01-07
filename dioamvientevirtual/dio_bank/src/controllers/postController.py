from flask import Blueprint, request, jsonify
from src.app import Post, db
from http import HTTPStatus

app = Blueprint("post", __name__, url_prefix="/posts")


def _create_post():
    data = request.json
    user = Post(username=data["username"])
    db.session.add(user)
    db.session.commit()


@app.route("/", methods=["GET", "POST"])
def handle_post():
    if request.method == "POST":
        _create_post()
        return {"message": "User Created"}, HTTPStatus.CREATED
    else:
        return {"posts": []}
