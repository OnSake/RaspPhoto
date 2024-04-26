from flash import Flask
import time
from grovepi import *
from picamera import PiCamera2, Preview



# --------------- Sensors --------------- #

picam = PiCamera2()
config = picam.create_preview_configuration()
picam.configure(config)


led_yellow_1 = 5
led_yellow_2 = 6
led_green = 7
button = 3


pinMode(led_yellow_1, "OUTPUT")
pinMode(led_yellow_2, "OUTPUT")
pinMode(led_green, "OUTPUT")
pinMode(button, "INPUT")

# --------------- Variables --------------- #
preview_status = False


# --------------- Fonctions --------------- #
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

def start_preview():
    preview_status = True
    picam.start()
    picam.start_preview()
    
def take_photo():
    if preview_status:
        print("ok")
    print("none")
      
def stop_preview():
    preview_status = False
    picam.stop_preview()
    picam.close()