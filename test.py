from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
import pypyodbc
import flask_login
import pyodbc


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

email = "fabricio"

cursor = connection.cursor()
SQLCommand = ("SELECT Email FROM Customers WHERE Email = '{0}'".format(email))
cursor.execute(SQLCommand)
emailResults = cursor.fetchone()

if emailResults:
    print("there's something there")
else:
    print('nothing there')
