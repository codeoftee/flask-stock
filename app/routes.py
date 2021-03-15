from datetime import timedelta

from flask import render_template, request, flash, url_for, redirect, session

from app import app, db
from app.models import User
from app.stock_functions import is_valid_email
import hashlib


@app.route('/')
@app.route('/home')
def home():
    if 'email' in session:
        email = session['email']
        hashed = session['hashed']
    else:
        email = request.cookies.get('UserEmail')
        hashed = request.cookies.get('Hashed')

    user = User.query.filter((User.email == email) & (User.password == hashed)).first()

    if user is None:
        return redirect(url_for('login_page'))

    return "Welcome to stock project {}".format(user.name)


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
        else:
            # hash submitted password
            password_hash = hashlib.sha256(password.encode())
            hashed = password_hash.hexdigest()
            user = User.query.filter((User.email == email) & (User.password == hashed)).first()

            if user is None:
                flash('Invalid email or password')
                return redirect(url_for('login_page'))

            # set sessions
            # python sessions https://pythonbasics.org/flask-sessions/
            session['email'] = email
            session['name'] = user.name
            session['hashed'] = hashed
            # set cookies
            # python cookies https://pythonbasics.org/flask-cookies/
            resp = redirect(url_for('home'))
            resp.set_cookie('UserEmail', email, max_age=timedelta(hours=24))
            resp.set_cookie('Hashed', hashed, max_age=timedelta(hours=24))
            resp.set_cookie('name', user.name, max_age=timedelta(hours=24))
            return resp


@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign-up.html')
    else:
        print('testing', request.form['name'])
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
        elif len(name) < 3:
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

            # hash submitted password
            password_hash = hashlib.sha256(password.encode())
            hashed = password_hash.hexdigest()
            user = User(name=name, phone=phone, gender=gender, password=hashed,
                        email=email)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('success'))


@app.route('/success')
def success():
    return render_template('success.html')
