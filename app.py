from fastai.vision import *
import cv2
from PIL import Image as PImage
import captrrue
import threading
import time
import firebaseBD
## config ##
ID_Device = 'VCuTbRfyv3146eIR3oSx'  # id ของถึงขยะ ตั้งค่าตาม firebase
Type = ['plastic','glass','metal','general'] 

NameImage ="null"
class dataImage: 
    def __init__(self, img = 0): 
         self._img = img
    # getter method 
    def get_img(self): 
        return self._img 
    # setter method 
    def set_img(self, img): 
        self._img = firebaseBD.UploadImage(img)  #ส่งค่ารูป ให้บันทึรูป


class Run:
    def index(self): # thread_function
        #main = threading.Thread(target=app.index(), args=(1,))
        learn = load_learner('E:/smart_bin_game_cs','model.pkl')
        while True :
            # print("Thread : 1")
            # time.sleep(3)
            status = False  #status semsor
             
            if(status == True ):
                image = captrrue.Cap() # cap in file captrue.py (import captrrue)
                print(type(image))
                pil_im = PImage.fromarray(image) 
                x = pil2tensor(pil_im ,np.float32)
                preds_num = learn.predict(Image(x)) #predict garbage
                print(('type : ',preds_num[0])) #name
                print(('data : ',preds_num)) #data all 

                if(preds_num[0] == '' or preds_num[0] == '' or preds_num[0] == '' or preds_num[0] == '' ):     # check  garbage 4 type
                    dataImage().set_img(image) #set img to class dataImage: 
                    firebaseBD.Insert_Data(preds_num[0],ID_Device,dataImage().get_img())
                    print('บันทึกเรียบร้อย +')

    def thread_function2(self):
        while True :
            print("Thread : 2") 
            time.sleep(1) 
    # def FirebaseSent(self):
    #     firebaseBD.
    def sensor(self): # ฟังชัน ตรวจจับขยะ เมื่อวางขยะลงถาดวางขยะ
        print('มีขยะ')


    def stepper(self):
        print('มอเตอร์ทำงาน')


#special valible
if __name__ == "__main__":
    #print(__name__)  #run index
    app = Run()
    app.index() 
    
       
    
    # app=APP() # pointer class APP: 
    # app.set_img(captrrue.Cap()) 
    # print(type(app.get_img()))

# learn = load_learner('E:/smart_bin_game_cs','model.pkl')
# image = captrrue.Cap() 
# print(type(image))
# pil_im = PImage.fromarray(image) 
# x = pil2tensor(pil_im ,np.float32)
# preds_num = learn.predict(Image(x))
# print(('type : ',preds_num[0]))
# print(('data : ',preds_num))
# GetImg(image)
# # cv2.waitKey(0)  

# def SetImg(img):

