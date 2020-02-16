import keras    
from keras.models import load_model, model_from_json
from keras.applications import ResNet50
from keras.preprocessing import image #*
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
#####
def Predict():
    # load
    model=ResNet50(weights='imagenet')###
    model = load_model('data/models/keras/model.h5')
    # load
    model.load_weights('data/models/keras/weights.h5')

    img_path = 'data/validation/glass/glass582.jpg'
    img = image.load_img(img, target_size=(224, 224))
    x = image.img_to_array(img_path)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    print(preds)
# cap = cv2.VideoCapture(0)
# cap.set(3, 224)
# cap.set(4, 224)
# __,img = cap.read()
# cv2.imshow('show',img)
Predict()
# cv2.waitKey(0)