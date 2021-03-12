from flask import render_template, request, flash, url_for

from app import app
from app.stock_functions import is_valid_email


@app.route('/')
@app.route('/home')
def home():
    return "Welcome to stock project"


@app.route('/login', methods=['POST', 'GET'])
def login_page():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        password = request.form['password']
        print('Submitted email is ', email)
        print('Submitted password is ', password)
        if email == '':
            flash('Invalid Email')
        elif password == '':
            flash('Invalid Password')

        if email == '' or password == '':
            return render_template('login.html')

        return "Email - {} Password - {}".format(email, password)

@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign-up.html')
    else:
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        gender = request.form['gender']
        password = request.form['password']
        password2 = request.form['password2']
        # validate fields
        validated = False
        if name == '' or phone == '' or email == '' or gender == '':
            flash('All fields are required!')
        elif len(name) < 3 or name[0].isnumeric:
            flash('Please enter a valid name!')
        elif not is_valid_email(email):
            flash('Email is invalid !')
        elif len(phone) != 11:
            flash('Invalid Phone Number!')
        elif password != password2:
            flash('Passwords does not match!')
        elif len(password) < 6:
            flash('Password is too short!')
        else:
            validated = True

        if not validated:
            return render_template('sign-up.html')
        else:
            print('Form submitted')