from contextlib import closing

from flask import Flask, redirect, render_template, request, url_for

from .db import get_connection, init_db
from .validation import validate_post


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=None,
    )

    if test_config:
        app.config.update(test_config)

    if app.config.get("DATABASE"):
        init_db(app)

    @app.get("/")
    def index():
        with closing(get_connection(app)) as connection:
            posts = connection.execute(
                "SELECT id, title, content FROM posts ORDER BY id DESC"
            ).fetchall()

        return render_template("index.html", posts=posts)

    @app.get("/new")
    def new_post():
        return render_template("new.html")

    @app.post("/create")
    def create_post():
        try:
            title, content = validate_post(
                request.form.get("title", ""),
                request.form.get("content", ""),
            )
        except ValueError:
            return redirect(url_for("new_post"))

        with closing(get_connection(app)) as connection:
            connection.execute(
                "INSERT INTO posts (title, content) VALUES (?, ?)",
                (title, content),
            )
            connection.commit()

        return redirect(url_for("index"))

    return app


def main():
    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
