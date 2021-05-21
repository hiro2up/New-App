from flask import Flask
from flask import request
app = Flask(__name__)
@app.route("/")#URL leading to method
def hello(): # Name of the method
 return("Hello World!")
@app.route("/greetme")#different URL
def helloall(): # different method name
 name = request.args.get('name')#retrieve GET parameters
 return("Hello {}!".format(name))#Python’s string.format
if __name__ == "__main__":
 app.run(debug=True) #Run the flask app at port 8080