import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import cv2
cred = credentials.Certificate('E:/smart_bin_game_cs/fir-db-8d065-firebase-adminsdk-3q9sr-12225edf78.json')
firebase_admin.initialize_app(cred)
img = cv2.imread('E:/smart_bin_game_cs/geeks.jpg')
bucket = storage.bucket('fir-db-8d065.appspot.com')
blob = bucket.blob('images/geeks.jpg',img)

print(blob)
