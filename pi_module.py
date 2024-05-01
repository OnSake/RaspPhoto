from flask import Flask
from flask_cors import CORS
import time
from datetime import datetime
from grovepi import *
from picamera import PiCamera



# --------------- Flask APP --------------- #

app = Flask(__name__)
cors = CORS(app, resources={r"*":{"origins": "*"}})#Pour autoriser toutes les requêtes



# --------------- Sensors --------------- #
led_yellow_1 = 2
led_yellow_2 = 3
led_green = 4


pinMode(led_yellow_1, "OUTPUT")
pinMode(led_yellow_2, "OUTPUT")
pinMode(led_green, "OUTPUT")

# --------------- Fonctions --------------- #
@app.route('/leds')
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
    return "leds lancées"

def take_shot(): #Prendre la photo
    date_today = datetime.now()
    nom_image = date_today.strftime('%d-%m-%Y_%Hh-%Mm-%Ss')
    picam = PiCamera()
    picam.start_preview()
    picam.capture('/var/www/html/RaspPhoto/assets/photos/'+nom_image+'.jpg')
    picam.stop_preview()
    picam.close()
    return nom_image


@app.route('/shot')

def shot():
    return take_shot()


if __name__ == '__main__':
    app.run(host='192.168.1.127', port=5000, debug=True) #Faire tourner le serveur python sur une adresse ip précise car sinon elle se met sur son adresse local 127.0.0.1:5000
#172.20.80.138
