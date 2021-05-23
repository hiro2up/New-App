from .__init__ import connection

def commitToDB(SQLCommand):

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
        self.user = fetchOneFromDB("SELECT * FROM Customers WHERE Email = '{0}'".format(inputEmail))
        self.id = self.user[0]
        self.email = self.user[1]
        self.firstName = self.user[3]
        self.lastName = self.user[4]
        self.addrline1 = self.user[5]
        self.addrline2 = self.user[6]
        self.city = self.user[7]
        self.eircode = self.user[8]

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