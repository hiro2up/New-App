# Here goes everything that IS related to authentication
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .__init__ import connection
from bs4 import BeautifulSoup
import requests
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user



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


        if emailResults[0] == email:
            if check_password_hash(str(passResults[0]),password):
                # user = email
                session['email'] = request.form['email']
                flash('Login successful', category='success')
                # login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Wrong password. Try again', category='error')
        else:
            flash('No account associated with {0} found'.format(email), category='error')
        # try:
            
        # except:
        #     flash('No account associated with {0} found'.format(email), category='error')

    return render_template("login.html", boolean=True)

@auth.route('/logout')
# @login_required
def logout():   
    session.pop('email',default=None)
    # logout_user()
    return redirect(url_for('auth.login'))

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

        cursor = connection.cursor()
        SQLCommand = ("SELECT Email FROM Customers WHERE Email = '{0}'".format(email1))
        cursor.execute(SQLCommand)
        emailResults = cursor.fetchone()


        if email1 != email2:
            flash('Emails do not match', category="error")
        elif len(email1) < 4:
            flash('Invalid email', category="error")
        elif emailResults:
            flash('E-mail already in use', category="error")
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
            session['email'] = request.form['email1']
            flash('Account created', category="success")
            # user = email1
            # login_user(user, remember=True)
            return redirect(url_for('views.home'))
    return render_template("signup.html")


@auth.route('/order', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        cursor = connection.cursor()
        customerId = cursor.execute("SELECT CustomerId FROM Customers WHERE Email = {0}".format(session.email))

        photo = request.form.get('photo')

        if request.form.get('size') == '70':
            size = "Small (12\"x16\") - €70"
        elif request.form.get('size') == '100':
            size = "Medium (16\"x24\") - €100"
        elif request.form.get('size') == '140':
            size = "Large (20\"x28\") - €140"
        else:
            size = "Extra Large (24\"x35\") - €200"

        if request.form.get('frame') == '30':
            frame = 'Yes (+ €30)'
        else:
            frame = 'No (+ €0)'
        
        if request.form.get('giftbox') == '20':
            giftbox = 'Yes (+ €20)'
        else:
            giftbox = 'No (+ €0)'
        
        addRequests = request.form.get('comment')
        totalAmount = request.form.get('total-amount')

        cursor = connection.cursor()
        if request.form.get('shipping-option') == 'No':
            addrline1 = request.form.get('ship-addr1')
            addrline2 = request.form.get('ship-addr2')
            city = request.form.get('ship-addr3')
            eircode = request.form.get('ship-addr4')
        else:
            cursor = connection.cursor()
            addrline1 = cursor.execute("SELECT AddrLine1 FROM Customers WHERE Email = {0}".format(session.email))
            addrline2 = cursor.execute("SELECT AddrLine2 FROM Customers WHERE Email = {0}".format(session.email))
            city = cursor.execute("SELECT City FROM Customers WHERE Email = {0}".format(session.email))
            eircode = cursor.execute("SELECT Eircode FROM Customers WHERE Email = {0}".format(session.email))

        #Add to database
        cursor = connection.cursor()
        SQLCommand = ("EXEC sp_NewOrder @CustomerId = '{0}', @Photo = \"{1}\", @Size = '{2}', @Frame = '{3}', @Giftbox = '{4}', @Requests = '{5}', @Amount = '{6}', @AddrLine1 = '{7}', @AddrLine2 = '{8}', @City = '{9}', @Eircode = '{10}';".format(customerId,photo,size,frame,giftbox,addRequests,totalAmount,addrline1,addrline2,city,eircode))
        cursor.execute(SQLCommand)

        flash('Order sent successfully', category="success")

    return render_template("order.html")
    

@auth.route('/myaccount')
def profile():
    return render_template("myaccount.html")