from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine, Table, Integer, Column, Identity, MetaData
from sqlalchemy.engine.base import Connection
from sqlalchemy.engine.url import URL
from sqlalchemy.sql.sqltypes import VARCHAR



connection_string = "{ODBC Driver 17 for SQL Server};SERVER=fabriciodb.dbsprojects.ie;DATABASE=FlaskMVC;UID=sa;PWD=Year20Server"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)

m = MetaData()
t = Table('t', m,
        Column('id', Integer, primary_key=True),
        Column('x', Integer))
m.create_all(engine)

# db = SQLAlchemy()
# DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kadsbu209dn38h83nd d3jdo32'


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app