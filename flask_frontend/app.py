from flask import Flask, render_template, url_for, send_from_directory
import requests
import os

app = Flask(__name__)

# The Django API base URL. When running locally, Django uses port 8000
API_BASE = os.environ.get("DJANGO_API_BASE", "http://127.0.0.1:8000/api")

@app.route("/")
def index():
    """
    Landing page with animated reveal.
    """
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    """
    Fetch gallery images from Django API.
    """
    resp = requests.get(f"{API_BASE}/photos/")
    photos = resp.json() if resp.ok else []
    return render_template("gallery.html", photos=photos)

@app.route("/final")
def final():
    return render_template("final.html")

@app.route("/puzzle")
def puzzle():
    return render_template("puzzle.html")

@app.route("/typewriter")
def typewriter():
    return render_template("typewriter.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route('/story')
def story():
    return render_template('story.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
