from flask import render_template

from app import app


@app.route('/')
@app.route('/home')
def home():
    return "Welcome to stock project"


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')
