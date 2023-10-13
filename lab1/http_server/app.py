#!/usr/local/bin/python3

from flask import Flask, send_from_directory, redirect
import random

app = Flask(__name__)


@app.route("/quote")
def inspiring_qoute():
    # source of quotes: https://www.ime.usp.br/~vwsetzer/jokes/Einstein-Quotes.html
    return f"Here you go - an inspiring quote: " + random.choice([
        "Any intelligent fool can make things bigger, more complex, and more violent. It takes a touch of genius -- and a lot of courage -- to move in the opposite direction.",
        "Imagination is more important than knowledge.",
        "The only real valuable thing is intuition.",
        "Everything should be made as simple as possible, but not simpler.",
        "Common sense is the collection of prejudices acquired by age eighteen.",
        "The secret to creativity is knowing how to hide your sources.",
        "The only thing that interferes with my learning is my education.",
        "The important thing is not to stop questioning. Curiosity has its own reason for existing."
    ])


@app.route("/")
def index():
    return redirect("/index.html")


@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


if __name__ == "__main__":
    # TODO-PRM: 2c) zmień poniższy port tak, aby zgadzał się on z portem w Dockerfile oraz w komendzie docker run
    app.run(host="0.0.0.0", port=..., debug=True)
