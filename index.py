from flask import Flask, render_template, request
from api import weather

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/getWeather', methods=['GET', 'POST'])
def get_weather():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        if request.form['city'] == "":
            error_message = "City cannot be empty, please select CITY."
            return render_template('index.html', error_message=error_message)

        else:
            app.logger.debug(weather.get_weather(request.form['city'], request.form['days']))
            typedata = type(weather.get_weather(request.form['city'], request.form['days']))
            weather1 = weather.get_weather(request.form['city'], request.form['days'])
            return render_template('index.html', weather=weather1)

if __name__ == '__main__':
    app.run(debug=True)
