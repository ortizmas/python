import os
import click

from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from flask_migrate import Migrate


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    active: Mapped[bool] = mapped_column(sa.Boolean, default=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"


class Post(db.Model):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(sa.String, nullable=False)
    body: Mapped[str] = mapped_column(sa.String, nullable=False)
    user_id: Mapped[int] = mapped_column(
        sa.Integer, sa.ForeignKey("user.id"), nullable=False
    )
    created: Mapped[datetime] = mapped_column(sa.DateTime, server_default=sa.func.now())

    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, title={self.title!r}, user_id={self.user_id!r})"


@click.command("init-db")
def init_db_command():
    global db
    """Clear the existing data and create new tables."""
    with current_app.app_context():
        db.create_all()
    click.echo("Initialized the database.")


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:///blog.sqlite",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # Register the database commands
    app.cli.add_command(init_db_command)

    # initialize extension
    db.init_app(app)
    migrate.init_app(app, db)

    # apply the blueprints to the app
    from src.controllers import userController, postController

    app.register_blueprint(userController.app)
    app.register_blueprint(postController.app)

    return app
