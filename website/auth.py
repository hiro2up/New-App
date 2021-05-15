# Here goes everything that IS related to authentication
from flask import Blueprint, render_template, request, url_for, flash
from . import connection
from bs4 import BeautifulSoup
import requests


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')

        cursor = connection.cursor()
        SQLCommand = ("SELECT Email FROM Users WHERE Email = '{0}'".format(email))
        cursor.execute(SQLCommand)
        results = cursor.fetchone()
        try:
            if results[0] == email:
                flash('Login successful', category='success')
            else:
                flash('No account associated with {0} found'.format(email), category='error')
        except:
            flash('No account associated with {0} found'.format(email), category='error')

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
        photo = request.form.get('photo')


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
            #learn how to insert image into database
            cursor = connection.cursor()
            SQLCommand = ("EXEC sp_NewUser @Email = '{0}', @Pass = '{1}', @FirstName = '{2}', @LastName = '{3}', @City = '{4}';".format(email1,password1,firstName,lastName,city))
            cursor.execute(SQLCommand)
            flash('Account created', category="success")
    return render_template("signup.html")

@auth.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        pass
        # url=url_for('static', filename='search.html')
        # content = requests.get(url).text
        # soup = BeautifulSoup(content, "value")
        # print(soup.prettify())

        # DESCOBRIR COMO INSERIR SHOW NO BANCO DE DADOS

    return render_template("search.html")

@auth.route('/profile')
def profile():
    return render_template("profile.html")


    #PAREI NA MESSAGE FLASHING 1:05:37