
import time
from grovepi import *
from picamera import PiCamera


led_yellow_1 = 5
led_yellow_2 = 6
led_green = 7
button = 4


pinMode(led_yellow_1, "OUTPUT")
pinMode(led_yellow_2, "OUTPUT")
pinMode(led_green, "OUTPUT")
pinMode(button, "INPUT")

def led_photo_shot():
    digitalWrite(led_yellow_1, 1)
    print("LED 1 ON")
    time.sleep(1.5)
    
    digitalWrite(led_yellow_2, 1)
    print("LED 2 ON")
    time.sleep(1.5)

    digitalWrite(led_green, 1)
    print("LED 3 ON")
    time.sleep(1.5)


    digitalWrite(led_yellow_1, 0)
    digitalWrite(led_yellow_2, 0)
    digitalWrite(led_green, 0)

active = True
while active == True:
    button_status = digitalRead(button)
    if button_status == 0:
        active = False
        led_photo_shot()
