from flask import Flask, render_template, request, redirect
import csv
from hn_scarape import *


def write_to_csv(data):
    with open('db.csv', newline='', mode='a') as db2:
        email = data['email']
        subject = data['subject']
        message = data['text']
        csv_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index.html')
def home2():
    return render_template('index.html')


@app.route('/works.html')
def works():
    return render_template('works.html')


@app.route('/hacker_news_scraper.html')
def scrape():
    return render_template('hacker_news_scraper.html', data=scraper())


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/thx.html')
def thx():
    return render_template('thx.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thx.html')
        except:
            return 'Did not saved to DB'
    else:
        return 'Something went wrong. Try again'


if __name__ == "__main__":
    app.run()