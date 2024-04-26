import tkinter as t
from PIL import Image, ImageTk, ImageGrab
from pi_module import *


fenetre = t.Tk()
fenetre.title("RaspPhoto")
fenetre.geometry("700x700")
fenetre.bind('<Escape>',lambda e: fenetre.destroy())


# --------------- PAGES --------------- #
home_frame =t.Frame(fenetre, background='#D5D5D5')
photo_frame =t.Frame(fenetre, background='#D5D5D5')

icon = Image.open("assets/icon/icon.png")
font = ('Poppins', 16, "bold")


# --------------- Home Page --------------- #
home_message = t.Label(home_frame, text="Bienvenue sur votre", background="#D5D5D5", font='Poppins').pack(fill='x', ipady=50)
home_img = icon.resize((170, 170))
home_tkimage = ImageTk.PhotoImage(home_img)
home_image = t.Label(home_frame, image=home_tkimage, background="#D5D5D5").pack()
home_title_message = t.Label(home_frame, text="RaspbPhoto", background="#D5D5D5", font=font).pack(fill='x', pady=20)
home_button = t.Button(home_frame, text='Prendre en photo', font= font, background='#BF046B', fg='#D1D5C6', activebackground='#3999BF').pack(pady=50)


# home_frame.pack(fill='both', expand=True)

# --------------- Photo Page --------------- #
photo_header = t.Frame(photo_frame, background='#D5D5D5')
photo_img = icon.resize((60, 60))
photo_tkimage = ImageTk.PhotoImage(photo_img)
photo_icon = t.Label(photo_header, image=photo_tkimage, background="#D5D5D5")
photo_title = t.Label(photo_header, text="RaspPhoto", font=font, background='#D5D5D5')

photo_preview = t.Frame(photo_frame, background='red')
photo_button = t.Frame(photo_frame, background='green')

photo_frame.pack(fill='both')
photo_header.pack(fill='x', side='top')
photo_icon.pack(side='left')
photo_title.pack(side='left', padx=10)

photo_preview.pack(expand=True, fill='both')
photo_button.pack(side='bottom', fill='both')


t.mainloop() #Laisser la fenetre ouverte