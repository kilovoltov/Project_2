from flask import Flask
from flask import render_template

import data


app = Flask(__name__)


@app.route('/')
def render_main():
    return render_template('index.html', title=data.title,
                           subtitle=data.subtitle,
                           description=data.description,
                           departures=data.departures,
                           tours=data.tours)


@app.route('/departures/<departure>/')
def render_departure(departure):
    items = dict(filter(lambda tour: tour[1]["departure"] == departure, data.tours.items()))
    departure = data.departures[departure]
    return render_template('departure.html', title=data.title,
                           departure=departure,
                           departures=data.departures,
                           tours=items)


@app.route('/tours/<int:id>/')
def render_tour(id):
    departure = data.departures[data.tours[id]["departure"]]
    return render_template('tour.html', title=data.title,
                           departure=departure,
                           departures=data.departures,
                           tour=data.tours[id])


if __name__ == '__main__':
    app.run(debug=True)
