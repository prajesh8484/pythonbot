import firebase_admin
from firebase_admin import credentials, db
import os

cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv('FIREBASE_DATABASE_URL')
})

def get_user_data(user_id):
    ref = db.reference(f'/users/{user_id}')
    return ref.get()

def update_user_data(user_id, data):
    ref = db.reference(f'/users/{user_id}')
    ref.set(data)

def get_all_users_data():
    ref = db.reference('/users')
    return ref.get()