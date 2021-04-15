import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# In order to get firebase credentials:
#   1. go to Project Settings
#   2. go to Service Accounts
#   3. 'Generate new private key'
#   4. Save as fbcredentials.json and put in same director as db.py
cred = credentials.Certificate("./fbcredentials.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sampleapp-875de-default-rtdb.firebaseio.com/'
})
ref = db.reference('/')

def store(path, data):
    ref.child(path).set(data)

def retrieve(path):
    return ref.child(path).get()