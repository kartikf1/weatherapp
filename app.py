from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def fun1():
    return render_template("index.html")


link = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=1cce1d3fdcf9b8e3576065bd845b8f4d"


@app.route('/weatherdata/', methods=["POST", "GET"])
def fun2():
    if request.method == "POST":
        city = request.form['city']
        a = link.format(city)
        api = requests.get(a).json()
        y = api['main']
        current_temprature = y['temp']
        humidity = y['humidity']
        tempmin = y['temp_min']
        tempmax = y['temp_max']

        # Coordinates
        x = api['coord']
        longtitude = x['lon']
        latitude = x['lat']

        # Country
        z = api['sys']
        country = z['country']
        citi = api['name']
        return render_template("weatherdata.html", city=citi, time=api['timezone'], country=country,
                               temp=current_temprature, temp_min=tempmin, temp_max=tempmax)


if __name__ == "__main__":
    app.run()
