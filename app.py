import requests
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/home')
def home():
    return render_template('index.html', results=results)

@app.route('/results', methods=['GET', 'POST'])
def results():
    url = 'https://data.cityofnewyork.us/resource/rc75-m7u3.json?date_of_interest={}'
    if request.method == 'GET':
        return f"The URL /results is accessed directly. Try going to '/home' to submit form"
    if request.method == 'POST':

        form = request.form
        date_of_interest = form['date']

        r = requests.get(url.format(date_of_interest)).json()

        results = {
            'date' : date_of_interest,
            'cases' : r[0]['case_count'],
            'hospitalized' : r[0]['hospitalized_count'],
            'deaths' : r[0]['death_count']
        }
        return render_template('results.html', results=results)

@app.route('/about')
def about():
    return render_template('about.html')
