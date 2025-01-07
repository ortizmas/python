from flask import Blueprint, request, jsonify
from src.app import User, db
from http import HTTPStatus
from sqlalchemy import inspect

app = Blueprint("user", __name__, url_prefix="/users")


def _create_user():
    data = request.json
    user = User(username=data["username"])
    db.session.add(user)
    db.session.commit()


def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    return [
        {
            "id": user.id,
            "username": user.username,
        }
        for user in users
    ]


@app.route("/", methods=["GET", "POST"])
def handle_user():
    if request.method == "POST":
        _create_user()
        return {"message": "User Created"}, HTTPStatus.CREATED
    else:
        return {"users": _list_users()}


@app.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = db.get_or_404(User, user_id)
    # user = User.query.get(user_id)
    # if user is None:
    #     return {"message": "User not found"}, HTTPStatus.NOT_FOUND
    return {"id": user.id, "username": user.username}


@app.route("/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    user = db.get_or_404(User, user_id)
    data = request.json

    # if "username" in data:
    #     user.username = data["username"]
    #     db.session.commit()

    # Other form to update the user
    mapper = inspect(User)
    for column in mapper.attrs:
        if column.key in data:
            setattr(user, column.key, data[column.key])
    db.session.commit()

    return {
        "id": user.id,
        "username": user.username,
    }


@app.route("/<int:user_id>/delete", methods=("POST",))
def delete(user_id):
    user = db.get_or_404(User, user_id)

    db.session.delete(user)
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT
