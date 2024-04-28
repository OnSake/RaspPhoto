from flask import Flask
from flask_cors import CORS
import time
from grovepi import *
from picamera import PiCamera


# --------------- Flask APP --------------- #
app = Flask(__name__)
CORS(app)

@app.route('/test')
def test():
    return 'wsh wsh canne a peche'


# --------------- Sensors --------------- #
led_yellow_1 = 5
led_yellow_2 = 6
led_green = 7
#button = 3


pinMode(led_yellow_1, "OUTPUT")
pinMode(led_yellow_2, "OUTPUT")
pinMode(led_green, "OUTPUT")
#pinMode(button, "INPUT")

# --------------- Variables --------------- #
preview_status = False


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

if __name__ == '__main__':
    app.run(host='192.168.1.127', port=5000, debug=True)


picam = PiCamera()
config = picam.create_preview_configuration()
picam.configure(config)


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


  #THIBAULT  
# import time
# from datetime import datetime
# from PIL import Image
# import os




# def PrisePhoto(NomPhoto): #prendre une photo avec Raspistill
#     command = "sudo raspistill -t 5000 -w 1200 -h 675 -o "+ NomPhoto +" -q 100" #prend une photo
#     os.system(command)

# def AfficherPhoto(NomPhoto): # affiche NomPhoto
#     print("loading image: " + NomPhoto)


# if (os.path.isdir("/home/pi/Desktop/Projet Photomaton/Photos_du_Photomaton") == False): # si le dossier pour stocker les photos n'existe pas       
#    os.mkdir("/home/pi/Desktop/Projet Photomaton/Photos_du_Photomaton")                  # alors on crée le dossier (sur le bureau)
#    os.chmod("/home/pi/Desktop/Projet Photomaton/Photos_du_Photomaton",0o777)            # et on change les droits pour pouvoir effacer des photos

# AfficherPhoto("/home/pi/Desktop/Projet Photomaton/accueil.png")
# #AfficherTexteAccueil("Installez-vous et appuyez sur le bouton pour prendre une photo")


# while True : #boucle jusqu'a interruption
#   try:
#         print ("\n attente boucle")
        
#         #on attend que le bouton soit pressé
        
            
#         """GPIO.wait_for_edge(24, GPIO.FALLING)""" #ne marche pas avec nos bp
#         # on a appuyé sur le bouton...


#         #on génère le nom de la photo avec heure_min_sec
#         date_today = datetime.now()
#         nom_image = date_today.strftime('%d-%m-%Y_%Hh-%Mm-%Ss')

        
#         #on déclenche la prise de photo
#         chemin_photo = '/home/pi/Desktop/photos/'+nom_image+'.jpeg'
#         PrisePhoto(chemin_photo) #Déclenchement de la prise de photo


#         #on affiche la photo
#         time.sleep(1)
#         AfficherPhoto(chemin_photo)


#         time.sleep(5) #Ajout d'un temps d'affichage afin de repartir sur l'accueil ensuite


#         #on recommence en rechargeant l'écran d'accueil
#         AfficherPhoto("/home/pi/Photomaton/accueil.png")
#         pygame.mixer.init()
#         son = pygame.mixer.Sound('/home/pi/Photomaton/son.wav')
#         canal = son.play()


#         """if GPIO.input(24) == : """#si le bouton est encore enfoncé (son etat sera 0)  /// ne marche pas avec nos bp
#         print ("Ho ; bouton  appuyé !!! Je dois sortir ; c'est le chef qui l'a dit !")
#         break # alors on sort du while 
 

#   except KeyboardInterrupt:
#     print ('sortie du programme!')
#     raise

# # reinitialisation GPIO lors d'une sortie normale


e
