# Here goes everything that IS related to authentication
from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import connection
from bs4 import BeautifulSoup
import requests
from werkzeug.security import generate_password_hash, check_password_hash
from .models import storePassword, verifyPassword




auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = str(request.form.get('password'))

        cursor = connection.cursor()
        SQLCommand = ("SELECT Email FROM Customers WHERE Email = '{0}'".format(email))
        cursor.execute(SQLCommand)
        emailResults = cursor.fetchone()

        cursor = connection.cursor()
        SQLCommand = ("SELECT Pass FROM Customers WHERE Email = '{0}'".format(email))
        cursor.execute(SQLCommand)
        passResults = cursor.fetchone()

        cursor = connection.cursor()
        SQLCommand = ("SELECT SaltPass FROM Customers WHERE Email = '{0}'".format(email))
        cursor.execute(SQLCommand)
        saltResults = cursor.fetchone()



        try:
            if emailResults[0] == email:
                if check_password_hash(str(passResults[0]),password):
                    flash('Login successful', category='success')
                    return redirect(url_for('views.home'))
                else:
                    flash('Wrong password. Try again', category='error')
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
        addr1 = request.form.get('addressline1')
        addr2 = request.form.get('addressline2')
        eircode = request.form.get('eircode')
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
        elif len(addr1) < 2:
            flash('Address is too short', category="error")
        elif len(eircode) < 7:
            flash('Invalid Eircode', category="error")
        elif password1 != password2:
            flash('Passwords do not match', category="error")
        elif len(password1) < 8:
            flash('Password is too short', category="error")
        else:
            #add to database
            #learn how to insert image into database
            hashedPass = generate_password_hash(password1,method='sha256')


            cursor = connection.cursor()
            SQLCommand = ("EXEC sp_NewCustomerH @Email = '{0}', @Pass = \"{1}\", @FirstName = '{2}', @LastName = '{3}', @AddrLine1 = '{4}', @AddrLine2 = '{5}', @City = '{6}', @Eircode = '{7}';".format(email1,hashedPass,firstName,lastName,addr1,addr2,city,eircode))
            #SQLCommand = ("EXEC sp_NewCustomer @Email = '{0}', @Pass = \"{1}\", @SaltPass = \"{2}\", @FirstName = '{3}', @LastName = '{4}', @AddrLine1 = '{5}', @AddrLine2 = '{6}', @City = '{7}', @Eircode = '{8}';".format(email1,hashedPass,salt,firstName,lastName,addr1,addr2,city,eircode))
            cursor.execute(SQLCommand)
            flash('Account created', category="success")
            return redirect(url_for('views.home'))
    return render_template("signup.html")

@auth.route('/order', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        pass

    return render_template("order.html")
    

@auth.route('/myaccount')
def profile():
    return render_template("myaccount.html")


    #PAREI NA MESSAGE FLASHING 1:05:37