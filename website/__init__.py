from flask import Flask
import pypyodbc


# connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=fabriciodb.dbsprojects.ie;DATABASE=database;UID=sa;PWD=Year20Server')

#Connection to the database using pypyodbc. The "connection" variable is used in other functions to fetch and commit data to the database 
# connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
# 'Server=fabriciodb.dbsprojects.ie;'
# 'Database=database;'
# 'encrypt=yes;'
# 'TrustServerCertificate=yes;'
# 'UID=sa;'
# 'PWD=Year20Server',autocommit = True)

def connectingDB():
    connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
    'Server=fabriciodb.dbsprojects.ie;'
    'Database=database;'
    'encrypt=yes;'
    'TrustServerCertificate=yes;'
    'UID=sa;'
    'PWD=Year20Server',autocommit = True)

    return connection

#####################################################################
# The set up for the app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kadsbu209dn38h83nd d3jdo32' #keyphrase to secure the app


    from .views import views #importing routes from the views.py file
    from .auth import auth #importing routes from the auth.py file

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app