from website import models
from flask import Flask, url_for, request
from flask_sqlalchemy import SQLAlchemy
import pypyodbc
import flask_login
import pyodbc
import base64


connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
'Server=fabriciodb.dbsprojects.ie;'
'Database=database;'
'encrypt=yes;'
'TrustServerCertificate=yes;'
'UID=sa;'
'PWD=Year20Server',autocommit = True)


def sendToDB(SQLCommand):

    cursor = connection.cursor()
    cursor.execute(SQLCommand)

def fetchOneFromDB(SQLCommand):

    cursor = connection.cursor()
    cursor.execute(SQLCommand)
    return cursor.fetchone()

def fetchAllFromDB(SQLCommand):
    cursor = connection.cursor()
    cursor.execute(SQLCommand)
    return cursor.fetchall()

# image = request.files['https://www.extremetech.com/wp-content/uploads/2019/12/SONATA-hero-option1-764A5360-edit.jpg']  
# image_string = base64.b64encode(image.read())
# print(image_string)

# custId = fetchOneFromDB("SELECT CustomerId from Customers WHERE Email = 'fabricio@msn.com'")[0]
# result = fetchAllFromDB("SELECT * FROM Orders WHERE CustomerId = {0}".format(int(custId)))
# for n in result:
#     print(n)

user = fetchAllFromDB("SELECT * FROM Customers WHERE Email = 'claire@re.com'")
print(user)