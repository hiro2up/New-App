import flask_login
from flask_login import login_manager, LoginManager
from flask_login.mixins import UserMixin
from .__init__ import connection
import pypyodbc

def sendToDB(SQLCommand):

    cursor = connection.cursor()
    cursor.execute(SQLCommand)

def fetchOneFromDB(SQLCommand):

    cursor = connection.cursor()
    cursor.execute(SQLCommand)
    return cursor.fetchone()
