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

pages = [home_frame, photo_frame]
icon = Image.open("assets/icon/icon.png")
font = ('Poppins', 16, "bold")


def home_page():
  for page in pages:
    page.pack_forget()
    home_frame.pack(fill='both', ipady=120)


def photo_page():
  for page in pages:
    page.pack_forget()
    photo_frame.pack(fill='both')

# --------------- Home Page --------------- #
home_message = t.Label(home_frame, text="Bienvenue sur votre", background="#D5D5D5", font='Poppins').pack(fill='x', ipady=50)
home_img = icon.resize((170, 170))
home_tkimage = ImageTk.PhotoImage(home_img)
home_image = t.Label(home_frame, image=home_tkimage, background="#D5D5D5").pack()
home_title_message = t.Label(home_frame, text="RaspbPhoto", background="#D5D5D5", font=font).pack(fill='x', pady=20)
home_button = t.Button(home_frame, text='Prendre en photo', font= font, background='#BF046B', fg='#D1D5C6', activebackground='#3999BF', command=photo_page).pack(pady=50)

# --------------- Photo Page --------------- #
photo_header = t.Frame(photo_frame, background='#D5D5D5')
photo_img = icon.resize((60, 60))
photo_tkimage = ImageTk.PhotoImage(photo_img)
photo_icon = t.Label(photo_header, image=photo_tkimage, background="#D5D5D5")
photo_title = t.Label(photo_header, text="RaspPhoto", font=font, background='#D5D5D5')

photo_preview = t.Frame(photo_frame, background='red')

photo_buttons = t.Frame(photo_frame, background='green')
photo_button = t.Frame(photo_buttons, background='black')
photo_button_gallery = t.Button(photo_button, text='Galerie', font= font, background='#BF046B', fg='#D1D5C6', activebackground='#3999BF')
photo_button_print = t.Button(photo_button, text='Imprimer', font= font, background='#BF046B', fg='#D1D5C6', activebackground='#3999BF')

photo_header.pack(fill='x', side='top')
photo_icon.pack(side='left')
photo_title.pack(side='left', padx=10)

photo_preview.pack(expand=True, fill='both')
photo_buttons.pack(side='bottom', fill='both')
photo_button.pack(expand=True, ipady=10, ipadx=10)
photo_button_gallery.pack(ipadx=50, side='left', padx=20)
photo_button_print.pack(ipadx=50, side='right', padx=20)

home_page()

t.mainloop() #Laisser la fenetre ouverte