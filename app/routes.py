from flask import Flask, render_template


def register_routes(app: Flask) -> None:
    @app.get("/")
    def home() -> str:
        return render_template("home.html")
