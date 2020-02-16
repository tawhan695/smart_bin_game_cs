from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.models import load_model, model_from_json
import cv2
from PIL import Image as PImage
import captrrue
import threading
import time
import firebaseBD
from controller import Move
#import numpy as np
# load model
model = ResNet50(weights='imagenet')
model = load_model('models/keras/model.h5')
model.load_weights('models/keras/weights.h5')

## config  รหัสถังขยะ ##
ID_Device = 'VCuTbRfyv3146eIR3oSx'  # id ของถึงขยะ ตั้งค่าตาม firebase
# Type = {'plastic':0,'glass':,'metal','general'} 
Type = {'glass': 0, 'metal': 0, 'plastic': 0,'general':0}
per = 50   # ความเเม่น ยำ ของโมเดล  ถ้าตำกว่า 50 ให้เป็นขนะทั่วไป
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
        #self.detectG()
        while True :
            Sensor =sensor(self)
            Distance  =  Sensor.getDistance() 
            
            print("รอขยะ ")
            if  int(Distance) <= 18:
                time.sleep(2) # รอ2วิ วางขยะ
                Garbage_name = self.detectG() #เรียนใช้ฟังชัน ถ่ายรูป และทำนาย
                if Garbage_name == 'glass':
                    print('ทิ้งช่อง 1 glass' )
                    firebaseBD.Insert_Data(Garbage_name,ID_Device,dataImage(self).get_img())
                    Move.Go(100)
                elif Garbage_name == 'metal':
                    print('ทิ้งช่อง 2 metal' )
                    firebaseBD.Insert_Data(Garbage_name,ID_Device,dataImage(self).get_img())
                    Move.Go(200)
                elif Garbage_name == 'plastic':
                    print('ทิ้งช่อง 3 plastic' )
                    firebaseBD.Insert_Data(Garbage_name,ID_Device,dataImage(self).get_img())
                    Move.Go(300)
                elif Garbage_name == 'general':
                    print('ทิ้งช่อง 4 general' )
                    firebaseBD.Insert_Data(Garbage_name,ID_Device,dataImage(self).get_img())
                    Move.Go(400)
    def detectG(self):
    ## ทำนายขยะ
        Max =0
        Garbage_name = 'general'
        try:
            image = captrrue.Cap() # cap in file captrue.py (import captrrue)
            x = image.img_to_array(img)
            dataImage(self).set_img(image)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            print('preds')
            preds = model.predict(x)
            data =preds[0]
            glass =data[0]
            metal =data[1]
            plastic =data[2]
            Type['glass']=int(data[0]*100)
            Type['metal']=int(data[1]*100)
            Type['plastic']=int(data[2]*100)

            if Type['glass'] => per :
                  if Max > Type['glass']:
                      Max = Type['glass']
                      Garbage_name ='glass'

            elif Type['metal'] => per:
                    if Max > Type['metal']:
                      Max = Type['metal']
                      Garbage_name ='metal'
                
            elif Type['plastic'] => per:
                    if Max > Type['plastic']:
                      Max = Type['plastic']  
                      Garbage_name ='plastic'          
            else :
                  Type['general'] = 100
                  Garbage_name ='general'

            print('Type',Type)
            print('Garbage_name',Garbage_name)

            return Garbage_name

        except :
            return 'error'

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

class sensor:
    distance =0
    def __init__(self):
        print('sensor start ..')
        self.ultrasonic_distance()
    def getDistance(self):
        print ("Distance:",self.distance,"cm")
        return self.distance
    def ultrasonic_distance(self):
        while True:
            try:
                GPIO.setmode(GPIO.BOARD)

                PIN_TRIGGER = 7
                PIN_ECHO = 11

                GPIO.setup(PIN_TRIGGER, GPIO.OUT)
                GPIO.setup(PIN_ECHO, GPIO.IN)

                GPIO.output(PIN_TRIGGER, GPIO.LOW)

                print ("Waiting for sensor to settle")

                time.sleep(1)

                print ("Calculating distance")

                GPIO.output(PIN_TRIGGER, GPIO.HIGH)

                time.sleep(0.00001)

                GPIO.output(PIN_TRIGGER, GPIO.LOW)

                while GPIO.input(PIN_ECHO)==0:
                        pulse_start_time = time.time()
                while GPIO.input(PIN_ECHO)==1:
                        pulse_end_time = time.time()

                pulse_duration = pulse_end_time - pulse_start_time
                distance = round(pulse_duration * 17150, 2)
                self.distance = distance
            finally:
                GPIO.cleanup()
#special valible
if __name__ == "__main__":
    print(__name__)  #run index
    Move(self).Home()
    sensor = threading.Thread(target=sensor.ultrasonic_distance, args=(1,))
    sensor.start() # ให้เซซ็นเซอร์ทำงาน
    app = Run() 
    app.index() 
    
       
    

