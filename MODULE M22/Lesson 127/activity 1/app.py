from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    age = None
    if request.method == "POST":
        dob = request.form.get("dob")
        birth = date.fromisoformat(dob)
        today = date.today()
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    return render_template("index.html", age=age)

if __name__ == "__main__":
    app.run(debug=True)
