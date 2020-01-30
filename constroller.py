from time import sleep
import RPi.GPIO as GPIO

class Move :
    DIR = 20   # Direction GPIO Pin
    STEP = 21  # Step GPIO Pin
    CW = 1     # Clockwise Rotation
    CCW = 0    # Counterclockwise Rotation
    SPR = 48   # Steps per Revolution (360 / 7.5) 

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.output(DIR, CW)

    step_count = [SPR,100,200, 300]  #48 ต่อ 1 รอบ
    delay = .0208
    ST = True
    End_stop = 0

    def Home(self): #ตอนเปิดเครื่อง
        print('Home')
        GPIO.output(self.DIR, self.CCW)
        
        while self.ST :
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(self.delay)
            print('รอ .. ')
            if(self.End_stop == 1):
                self.ST = False
        print('ถึงตำแหน่ Home')
    def Go(self,i):
        print('เคลื่นที่ไปข้างหน้า')
        for self.x in range(self.step_count[i]): 
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(self.delay)
    def Back(self):
        print('เคลื่นที่กลับ')
        GPIO.output(self.DIR, self.CCW)
        while self.ST :
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(self.delay)
            print('รอ .. ')
            if(self.End_stop == 1):
                self.ST = False
        print('ถึงตำแหน่ Home')