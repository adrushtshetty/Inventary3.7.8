from flask import Flask, request, jsonify, render_template, url_for, redirect
from csv import writer
import pandas as pd
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'androengrsupt' or request.form['password'] != 'cnooc114':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home_page'))
    return render_template('login.html', error=error)

@app.route('/home')
def home_page():
    return render_template("index.html")

@app.route('/interview_form')
def interview():
    return render_template("forms-elements.html")


@app.route('/eo_form')
def query_page():
    return render_template('eo_Form.html')


if __name__ == '__main__':
    app.run(debug=True)