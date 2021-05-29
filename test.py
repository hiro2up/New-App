import unittest, pytest
from website.models import Customer, Order
from website import auth, connectingDB
import app, pypyodbc
from app import app
# from flask.testing import FlaskClient
# import flask_testing


#Testing pypyodbc connection with Database
#connectingDB() is imported from models.py
class TestDBConnection(unittest.TestCase):
    def test_Connection(self):
        self.assertIsInstance(connectingDB(),pypyodbc.Connection)


#Testing classes
#the classes are imported from models.py
class ClassesTest(unittest.TestCase):

    def setUp(self):
        self.email = 'claire@re.com'
        connectingDB()
    
    #testing for the result info being fetched
    def test_fetch_Customer(self):
        result = Customer(self.email)
        self.assertEqual(result.id,10)

    #testing for the result type
    def test_fetch_Order(self):
        result = Order(self.email)
        self.assertIsInstance(result.ordersList,list)


#Testing Routes
#taken from https://stackoverflow.com/questions/31710064/testing-flask-routes-do-and-dont-exist
#In this piece of code we're testing an existing and non-existing route against the expected status
#Using 
class RouteTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.c = app.test_client()

    def test_login(self):
        self.response = self.c.get('/login')
        self.assertEqual(self.response.status_code,200)

    def test_nonexist_route(self):
        self.response = self.c.get('/newpage')
        self.assertEqual(self.response.status_code,404)



if __name__ == '__main__':
    unittest.main()