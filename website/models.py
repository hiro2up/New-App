from .__init__ import connection
import pypyodbc

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

class Customer:
    def __init__(self,inputEmail):
        self.id = fetchOneFromDB("SELECT CustomerId FROM Customers WHERE Email = '{0}'".format(inputEmail))[0]
        self.email = inputEmail
        self.password = fetchOneFromDB("SELECT Pass FROM Customers WHERE Email = '{0}'".format(inputEmail))[0]
        self.firstName = fetchOneFromDB("SELECT FirstName FROM Customers WHERE Email = '{0}'".format(inputEmail))[0]
        self.lastName = fetchOneFromDB("SELECT LastName FROM Customers WHERE Email = '{0}'".format(inputEmail))[0]
        self.addrline1 = fetchOneFromDB("SELECT AddrLine1 FROM Customers WHERE Email = '{0}'".format(inputEmail))[0]
        self.addrline2 = fetchOneFromDB("SELECT AddrLine2 FROM Customers WHERE Email = '{0}'".format(inputEmail))[0]
        self.city = fetchOneFromDB("SELECT City FROM Customers WHERE Email = '{0}'".format(inputEmail))[0]
        self.eircode = fetchOneFromDB("SELECT Eircode FROM Customers WHERE Email = '{0}'".format(inputEmail))[0]

class Order:
    def __init__(self,inputCustEmail):
        self.custId = fetchOneFromDB("SELECT CustomerId from Customers WHERE Email = '{0}'".format(inputCustEmail))[0]
        self.ordersList = fetchAllFromDB("SELECT * FROM Orders WHERE CustomerId = '{0}'".format(self.custId))
        
        #[0] OrderId
        #[1] CustomerId
        #[2] Photo
        #[3] Size
        #[4] Requests
        #[5] Frame
        #[6] Giftbox
        #[7] AddrLine1
        #[8] AddrLine2
        #[9] City
        #[10] Eircode