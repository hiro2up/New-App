# Here goes everything that IS related to authentication
from flask import Blueprint, render_template, request, url_for, flash
import flask


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logput</p>"

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email1 = request.form.get('email1')
        email2 = request.form.get('email2')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        city = request.form.get('city')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        if email1 != email2:
            flash('Emails do not match', category="error")
        elif len(email1) < 4:
            flash('Invalid email', category="error")
        elif len(firstName) < 2:
            flash('First name too short', category="error")
        elif len(lastName) < 2:
            flash('Last name too short', category="error")
        elif len(city) < 2:
            flash('City name too short', category="error")
        elif password1 != password2:
            flash('First name too short', category="error")
        elif len(password1) < 8:
            flash('Password is too short', category="error")
        else:
            #add to database
            #PAREI NA MESSAGE FLASHING
            flash('Account created', category="success")
    return render_template("signup.html")

@auth.route('/search', methods=['GET','POST'])
def search():
    return render_template("search.html")