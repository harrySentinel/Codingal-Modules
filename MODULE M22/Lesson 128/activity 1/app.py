from flask import Flask, render_template, request

app = Flask(__name__)

def predict_weather(temp, humidity, wind):
    if humidity > 80 and temp < 20:
        return "Rainy", "🌧️"
    elif humidity > 70 and wind > 30:
        return "Stormy", "⛈️"
    elif temp > 35 and humidity < 40:
        return "Sunny & Hot", "☀️"
    elif temp > 25 and humidity < 60:
        return "Clear & Pleasant", "🌤️"
    elif temp < 10:
        return "Cold", "🥶"
    else:
        return "Cloudy", "☁️"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    icon = None
    if request.method == "POST":
        temp     = float(request.form.get("temp"))
        humidity = float(request.form.get("humidity"))
        wind     = float(request.form.get("wind"))
        weather, icon = predict_weather(temp, humidity, wind)
    return render_template("index.html", weather=weather, icon=icon)

if __name__ == "__main__":
    app.run(debug=True)
