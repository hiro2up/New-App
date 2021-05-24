# Here goes everything that IS related to authentication
from pypyodbc import DATETIME
from website.models import fetchOneFromDB, commitToDB, Customer, Order, fetchAllFromDB
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = str(request.form.get('password'))

        emailResults = fetchOneFromDB("SELECT Email FROM Customers WHERE Email = '{0}'".format(email))
        passResults = fetchOneFromDB("SELECT Pass FROM Customers WHERE Email = '{0}'".format(email))

        
        try:
            if emailResults[0] == email:
                if check_password_hash(str(passResults[0]),password):
                    session['email'] = request.form['email']
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
    session.pop('email',default=None)
    flash('Log out successful', category='success')
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

        emailResults = fetchOneFromDB("SELECT Email FROM Customers WHERE Email = '{0}'".format(email1))


        if email1 != email2:
            flash('Emails do not match', category="error")
        elif len(email1) < 5:
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
            hashedPass = generate_password_hash(password1,method='sha256')

            commitToDB("EXEC sp_NewCustomerH @Email = '{0}', @Pass = \"{1}\", @FirstName = \"{2}\", @LastName = \"{3}\", @AddrLine1 = \"{4}\", @AddrLine2 = \"{5}\", @City = \"{6}\", @Eircode = \"{7}\";".format(email1,hashedPass,firstName,lastName,addr1,addr2,city,eircode))

            session['email'] = request.form['email1']
            flash('Account created', category="success")
            return redirect(url_for('views.home'))
    return render_template("signup.html")


@auth.route('/order', methods=['GET','POST'])
def order():
    if request.method == 'POST':
        customerId_fetch = fetchOneFromDB("SELECT CustomerId FROM Customers WHERE Email = '{0}'".format(session['email']))
        customerId = int(customerId_fetch[0])

        # image = request.files['photo']  
        # photob64 = base64.b64encode(image.read())

        photo = request.form.get('photo')

        if request.form.get('size') == '70':
            size = "Small (12x16) - €70"
        elif request.form.get('size') == '100':
            size = "Medium (16x24) - €100"
        elif request.form.get('size') == '140':
            size = "Large (20x28) - €140"
        else:
            size = "Extra Large (24x35) - €200"

        if request.form.get('frame') == '30':
            frame = 'Yes (+ €30)'
        else:
            frame = 'No (+ €0)'
        
        if request.form.get('giftbox') == '20':
            giftbox = 'Yes (+ €20)'
        else:
            giftbox = 'No (+ €0)'
        
        addRequests = request.form.get('comment')
        totalAmount = int(str(request.form.get('total-amount'))[2:])

        if request.form.get('shipping-option') == 'No':
            addrline1 = request.form.get('ship-addr1')
            addrline2 = request.form.get('ship-addr2')
            city = request.form.get('ship-addr3')
            eircode = request.form.get('ship-addr4')
        else:
            addrline1 = fetchOneFromDB("SELECT AddrLine1 FROM Customers WHERE Email = '{0}'".format(session['email']))[0]
            addrline2 = fetchOneFromDB("SELECT AddrLine2 FROM Customers WHERE Email = '{0}'".format(session['email']))[0]
            city = fetchOneFromDB("SELECT City FROM Customers WHERE Email = '{0}'".format(session['email']))[0]
            eircode = fetchOneFromDB("SELECT Eircode FROM Customers WHERE Email = '{0}'".format(session['email']))[0]
            
        timestamps = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #Add to database
        #commitToDB("EXEC sp_NewOrder @CustomerId = {0}, @Photo = \"{1}\", @Size = \"{2}\", @Frame = \"{3}\", @Giftbox = \"{4}\", @Requests = \"{5}\", @Amount = {6}, @AddrLine1 = \"{7}\", @AddrLine2 = \"{8}\", @City = \"{9}\", @Eircode = \"{10}\";".format(customerId,photo,size,frame,giftbox,addRequests,totalAmount,addrline1,addrline2,city,eircode))
        commitToDB("EXEC sp_NewOrder @CustomerId = {0}, @Photo = '{1}', @Size = '{2}', @Frame = '{3}', @Giftbox = '{4}', @Requests = '{5}', @Amount = {6}, @AddrLine1 = \"{7}\", @AddrLine2 = \"{8}\", @City = \"{9}\", @Eircode = \"{10}\", @Timestamps = \"{11}\";".format(customerId,photo,size,frame,giftbox,addRequests,totalAmount,addrline1,addrline2,city,eircode,timestamps))
        

        flash('Order sent successfully', category="success")

    try:
        if session['email'] != None:
            return render_template("order.html")
    except:
        flash('You must login to access this page', category="error")
        return redirect(url_for('auth.login'))
    

@auth.route('/myaccount', methods=['GET','POST'])
def myaccount():

    custId = fetchOneFromDB("SELECT CustomerId FROM Customers WHERE Email = '{0}'".format(session['email']))
    nOrders = fetchOneFromDB("SELECT COUNT (*) FROM Orders WHERE CustomerId = {0}".format(int(custId[0])))[0]
    print(nOrders)

    if request.method == 'POST':
        updFirstName = request.form.get('upd-firstName')
        updLastName = request.form.get('upd-lastName')
        updAddrLine1 = request.form.get('upd-addrline1')
        updAddrLine2 = request.form.get('upd-addrline2')
        updCity = request.form.get('upd-city')
        updEircode = request.form.get('upd-eircode')

        updlist = [updFirstName,updLastName,updAddrLine1,updAddrLine2,updCity,updEircode]

        if updFirstName == '' or updLastName == '' or updAddrLine1 == '' or updAddrLine2 == '' or updCity == '' or updEircode == '':
            flash('All fields are required', category='error')
        else:
            commitToDB("EXEC sp_UpdateCustomer @FirstName = \"{0}\", @LastName = \"{1}\", @AddrLine1 = \"{2}\", @AddrLine2 = \"{3}\", @City = \"{4}\", @Eircode = \"{5}\", @Email = '{6}'".format(updFirstName,updLastName,updAddrLine1,updAddrLine2,updCity,updEircode,session['email']))
            #commitToDB("EXEC sp_UpdateCustomer @FirstName = '{0}', @LastName = '{1}', @AddrLine1 = '{2}', @AddrLine2 = '{3}', @City = '{4}', @Eircode = '{5}', @Email = '{6}'".format(updFirstName,updLastName,updAddrLine1,updAddrLine2,updCity,updEircode,session['email']))
            flash('Account info updated successfully', category='success')
        

    try:
        if session['email'] != None:
            return render_template("myaccount.html",user = Customer(str(session['email'])), orders = Order(str(session['email'])), nOrd = nOrders)
    except:
        flash('You must login to access this page', category="error")
        return redirect(url_for('auth.login'))