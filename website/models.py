import pypyodbc, regex

with open('.pw') as file:
    password = file.read()

def connectingDB():
    connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
    'Server=fabriciodb.dbsprojects.ie;'
    'Database=database;'
    'encrypt=yes;'
    'TrustServerCertificate=yes;'
    'UID=sa;'
    'PWD='+password,autocommit = True)

    return connection

#Functions to commit to and fetch data from database
def commitToDB(SQLCommand):

    #cursor = connection.cursor()
    cursor = connectingDB().cursor()
    cursor.execute(SQLCommand)

def fetchOneFromDB(SQLCommand):

    #cursor = connection.cursor()
    cursor = connectingDB().cursor()
    cursor.execute(SQLCommand)
    return cursor.fetchone()

def fetchAllFromDB(SQLCommand):
    #cursor = connection.cursor()
    cursor = connectingDB().cursor()
    cursor.execute(SQLCommand)
    return cursor.fetchall()

#Checking password rules (Using regex)
#It must contain at least: 1 small letter, 1 capital letter, 1 special character, 1 digit, minimum length 8 and cannot contain spaces
def passwordCheck(password):
    needle_no = ['[Pp][Aa4][Ss5]{2}[Ww][Oo0][Rr][Dd]','\s+'] #cannot contain
    needle_yes = ['\d+','[A-Z]+','[a-z]+','\W','.{8}'] #must contain
    base_no = []
    base_yes =[]
    for no in needle_no:
        base_no.append(regex.compile(no))
    for yes in needle_yes:
        base_yes.append(regex.compile(yes))
    
    count = 0
    for bn in base_no:
        test = bn.search(password)
        if test is not None:
            count+=1

    for by in base_yes:
        test = by.search(password)
        if test is None:
            count+=1
    #for each fail, it'll increase count by 1. If all pass, count = 0
    return count

#Customer and Order classes
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
        #[5] TotalAmount
        #[6] Frame
        #[7] Giftbox
        #[8] AddrLine1
        #[9] AddrLine2
        #[10] City
        #[11] Eircode
        #[12] Status
        #[13] Timestamp
