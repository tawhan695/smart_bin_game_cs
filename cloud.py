import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase
from datetime import datetime
import time
now = datetime.now()
dt_string = now.strftime("%d-%m-%Y,%H:%M:%S")
# Use a service account



# data = {
#     u'GarbageType': u'Hello, World!',
#     u'Image': True,
#     u'numberExample': 3.14159265,
#     u'DateTime': datetime.now(),
#     u'Location': [5, True, u'hello'],
   
# }

# print(db.collection(u'users').document().set(data))

# doc_ref = db.collection(u'users').document(u'3333')
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 44444
# })