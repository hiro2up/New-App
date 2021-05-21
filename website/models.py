import flask_login
from flask_login import login_manager, LoginManager

import hashlib
import random
import base64

# Storing and verifying hashed Password
def storePassword(password):
  salt = str(random.randint(0,2**64)).encode('utf-8')
  return(salt,base64.b64encode(hashlib.sha256(salt+password.encode('utf-8')).digest()))

def verifyPassword(password,pwhash):
  return base64.b64encode(hashlib.sha256(pwhash[0]+password.encode('utf-8')).digest())==pwhash[1]