import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import datetime as dtime

import sys
### Add Path For Testing This File Only
sys.path.append("C:\\Users\\Paoyimpae\\Desktop\\FaceEyePassword\\")

### Firebase Setting ###
cred = credentials.Certificate('../json/Admin_SDK.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

### Date and Time Instance ###
dateTime = dtime.datetime.now()

### Adding Data ###

# Date and Time Getting (Now)
date = dtime.datetime.now().date().strftime('%d %b %Y'), 
time = dtime.datetime.now().time().strftime('%H:%M:%S'),

# Face Detection Password Getting (4-Digit)
now_pw = ['M', 'L', 'R', 'L']

# # Add Data From Face Detection
# doc_ref = db.collection(u'face_recognition').document()
# doc_ref.set({
#     u'name': u'Paoyimpae', # Now (Force-Data)
#     u'date': date,
#     u'time': time,
#     u'input_code': now_pw # If program gets 4-digit of password
# })

# doc_ref = db.collection(u'register').document()
# doc_ref.set({
#     u'name': u'Paoyimpae', # Now (Force-Data)
#     u'password': now_pw # If program gets 4-digit of password
# })

# doc_ref = db.collection(u'result').document()
# doc_ref.set({
#     u'name': u'Paoyimpae', # Now (Force-Data)
#     u'date': date,
#     u'time': time
# })
