import flask_login
from flask_login import login_manager, LoginManager
from flask_login.mixins import UserMixin
from . import connection

# User class
# class User(UserMixin):
#   cursor = connection.cursor()
#   SQLCommand = ("SELECT CustomerId FROM Customers")
#   cursor.execute(SQLCommand)
#   idResults = cursor.fetchone()

#   cursor = connection.cursor()
#   SQLCommand = ("SELECT Email FROM Customers")
#   cursor.execute(SQLCommand)
#   emailResults = cursor.fetchone()
  
#   user_id = idResults
#   user_email = emailResults