from flask import Flask, url_for, request
from flask_sqlalchemy import SQLAlchemy
import pypyodbc
import flask_login
import pyodbc
import base64

...

image = request.files['https://www.extremetech.com/wp-content/uploads/2019/12/SONATA-hero-option1-764A5360-edit.jpg']  
image_string = base64.b64encode(image.read())
print(image_string)
