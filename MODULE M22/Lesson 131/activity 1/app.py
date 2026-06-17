from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "codingal_secret_key"

users = {
    "aditya": "codingal123",
    "riya": "password1",
    "aman": "password2"
}

@app.route("/")
def index():
    if "username" in session:
        return render_template("dashboard.html", username=session["username"])
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    message = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("index"))
        else:
            message = "Invalid username or password!"
    return render_template("login.html", message=message)

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
