import pyrebase
from datetime import datetime
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


now = datetime.now()
dt_string = now.strftime("%d-%m-%Y,%H:%M:%S")
timestamp = datetime.timestamp(now)


## config ##
# ID_Device = 'VCuTbRfyv3146eIR3oSx'
# Type ={'1','2','3','4'}



def Insert_Data(GarbageType,BinID,PathImg):
  cred = credentials.Certificate ( "fir-db-8d065-firebase-adminsdk-3q9sr-12225edf78.json" ) 
  firebase_admin.initialize_app(cred)
  db = firestore.client()
  data = {
    u'GarbageType': str(GarbageType),
    u'Image': PathImg,
    u'DateTime': datetime.now(),
    u'BinID': str(BinID),
    }
  db.collection(u'Data_Garbage').document().set(data)


def UploadImage(img):
    firebaseConfig = {
        "apiKey": "AIzaSyBlgB3Up0iQSHwjjeKKv4fVS5nbjeCjHvM",
        "authDomain": "fir-db-8d065.firebaseapp.com",
        "databaseURL": "https://fir-db-8d065.firebaseio.com",
        "projectId": "fir-db-8d065",
        "storageBucket": "fir-db-8d065.appspot.com",
        "messagingSenderId": "417540815548",
        "appId": "1:417540815548:web:6eb2526ba2cc39a68f2eb9",
        "measurementId": "G-QZQXP66PJW"
      }
    firebase=pyrebase.initialize_app(firebaseConfig)
    storage =firebase.storage()
    name =storage.child('images/'+str(dt_string)+'.jpg').put(img)#".sv": "timestamp"
    imgUrl =storage.child(name['name']).get_url(name['downloadTokens'])
    return str(imgUrl)
