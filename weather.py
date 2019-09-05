from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/output', methods=['POST'])
def output():
    city_name = request.form['cityname']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&APPID=12585434db32732055c534824be5a420')
    json_object = r.json()

    maxtemp_k = float(json_object['main']['temp_max'])
    maxtemp_c = round((maxtemp_k - 273.15), 1)

    sunset_e = json_object['sys']['sunset']
    sunset_t = datetime.fromtimestamp(sunset_e)

    return render_template('output.html', temp_max=maxtemp_c, sunset=sunset_t)

if __name__ == '__main__':
	app.run(debug=True)
