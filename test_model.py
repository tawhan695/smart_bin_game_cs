from fastai.vision import *
import cv2
from PIL import Image as PImage
import time 
print('delay 3 sc')
# time.sleep(3)
# cap  = cv2.VideoCapture(0)
learn = load_learner('E:/smart_bin_game_cs','export.pkl')
print(learn.data)
# img = cv2.imread('data/train/cardboard/cardboard12.jpg')
# img = cv2.imread('data/train/metal/metal7.jpg')
img = cv2.imread('data/train/plastic/plastic5.jpg')
# ret, frame = cap.read()
# img = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)
pil_im = PImage.fromarray(img) 
x = pil2tensor(pil_im ,np.float32)
preds_num = learn.predict(Image(x))
print(preds_num[1])
# preds_num = learn.predict(img) #predict garbage
# print(('type : ',preds_num[3])) #name
print((preds_num)) #data all
# cv2.imwrite('type::'+str(preds_num[0])+'.jpg',img)
# cv2.imshow(''+str(preds_num[3]),img) 
# cv2.waitKey(0)
# # print(type(img))
# pil_im = Image.fromarray(img) 
# x = pil2tensor(img ,np.float32)
