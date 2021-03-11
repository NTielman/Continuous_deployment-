from flask import Flask, redirect, url_for
from datetime import date, timedelta

app = Flask(__name__)

current_day = date.today()


@app.route('/')
def index():
    return f'Today is {current_day.isoformat()}'


@app.route('/today/')
def today():
    return redirect(url_for('index'))


@app.route('/tomorrow/')
def tomorrow():
    next_day = current_day + timedelta(days=1)
    return f'Tomorrow is {next_day.isoformat()}'


@app.route('/yesterday/')
def yesterday():
    prev_day = current_day - timedelta(days=1)
    return f'Yesterday was {prev_day.isoformat()}'


if __name__ == "__main__":
    app.run()