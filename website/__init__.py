from flask import Flask, url_for, session
from flask_login import login_manager
from flask_sqlalchemy import SQLAlchemy
import pypyodbc
import flask_login
import pyodbc
from flask_login import LoginManager


# from sqlalchemy import create_engine, Table, Integer, Column, MetaData#, Identity
# from sqlalchemy.engine.base import Connection
# from sqlalchemy.engine.url import URL
# from sqlalchemy.sql.sqltypes import VARCHAR

# connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=fabriciodb.dbsprojects.ie;DATABASE=database;UID=sa;PWD=Year20Server')

connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
'Server=fabriciodb.dbsprojects.ie;'
'Database=database;'
'encrypt=yes;'
'TrustServerCertificate=yes;'
'UID=sa;'
'PWD=Year20Server',autocommit = True)

# cursor = connection.cursor()
# SQLCommand = ("CREATE DATABASE Customer;")
# cursor.execute(SQLCommand)
# print('done')
# connection.close()

#####################################################################
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kadsbu209dn38h83nd d3jdo32'

    


    from .views import views
    from .auth import auth
    # from .models import User

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    # login_manager.init_app(app)

    # @login_manager.user_loader
    # def load_user(id):
    #     from . import connection
    #     cursor = connection.cursor()
    #     SQLCommand = ("SELECT CustomerId FROM Customers")
    #     cursor.execute(SQLCommand)
    #     idResults = cursor.fetchone()
    #     return User.idResults

    return app