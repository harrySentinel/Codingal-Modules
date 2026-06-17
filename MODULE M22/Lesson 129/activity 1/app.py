from flask import Flask, render_template, request
import folium

app = Flask(__name__)

CITIES = {
    "mumbai":    (19.0760, 72.8777),
    "delhi":     (28.6139, 77.2090),
    "bangalore": (12.9716, 77.5946),
    "chennai":   (13.0827, 80.2707),
    "pune":      (18.5204, 73.8567),
    "kolkata":   (22.5726, 88.3639),
    "hyderabad": (17.3850, 78.4867)
}

@app.route("/", methods=["GET", "POST"])
def index():
    map_html = None
    city_name = None
    if request.method == "POST":
        city = request.form.get("city").lower().strip()
        if city in CITIES:
            lat, lon = CITIES[city]
            city_name = city.title()
            m = folium.Map(location=[lat, lon], zoom_start=12)
            folium.Marker([lat, lon], popup=city_name,
                          tooltip=f"📍 {city_name}").add_to(m)
            map_html = m._repr_html_()
        else:
            city_name = "City not found"
    return render_template("index.html", map_html=map_html, city=city_name)

if __name__ == "__main__":
    app.run(debug=True)
