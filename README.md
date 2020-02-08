# smart_bin_game_cs

** เพิ่มไฟล์ controller.py   [30/1/2020]**
```
ตั้งค่า pin
    DIR = 20   # Direction GPIO Pin
    STEP = 21  # Step GPIO Pin

ฟังชันทำงานตอนเปิดเครื่อง  def Home(self)
ฟังชันเคลื่นที่ไป ยังช่องถัง def Go(self,i): 
         รับตัวแปลจาก i เพื่อระบุตำแหน่ง ช่องที่จะไปเทขยะ
        ตัวแปล array ของตำแหน่งถัง     step_count = [50,100,200, 300]  
        ** step_count[0] จะมีค่า = 50
           step_count[1] จะมีค่า = 100
           step_count[2] จะมีค่า = 200   ใช้ส่งให้มอเตอร์ หมุน 200 step
           step_count[3] จะมีค่า = 300
        **
        
ฟังชันเคลื่นที่กลับที่เิ่มต้น def Back(self):
  
อ้างอิง https://www.rototron.info/raspberry-pi-stepper-motor-tutorial/
```
--ติดตั้ง fastai 
```
pip3 install fastai

```
--ติดตั้ง เชื่อมต่อกับ firebase
```
1. pip3 install Pyrebase
2. pip3 install firebase-admin
```
pip3 install opencv-python==3.4.6.27