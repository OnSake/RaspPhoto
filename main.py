import tkinter as t
from PIL import Image, ImageTk, ImageGrab


fenetre = t.Tk()
fenetre.title("RaspPhoto")
fenetre.geometry("700x700")
fenetre.bind('<Escape>',lambda e: fenetre.destroy())


# --------------- PAGES --------------- #
home_frame =t.Frame(fenetre, background='#D5D5D5')
photo_frame =t.Frame(fenetre, background='#000000')


font = ('Poppins', 16, "bold")


# --------------- Home Page --------------- #
home_message = t.Label(home_frame, text="Bienvenue sur votre", background="#D5D5D5", font='Poppins').pack(fill='x', ipady=50)
home_img = Image.open("assets/icon/icon.png")
home_img = home_img.resize((170, 170))
home_tkimage = ImageTk.PhotoImage(home_img)
home_image = t.Label(home_frame, image=home_tkimage, background="#D5D5D5").pack()
home_title_message = t.Label(home_frame, text="RaspbPhoto", background="#D5D5D5", font=font).pack(fill='x', pady=20)
home_button = t.Button(home_frame, text='Prendre en photo', font= font, background='#BF046B', fg='#D1D5C6', activebackground='#3999BF').pack(pady=50)


#home_frame.pack(fill='both', expand=True)


# --------------- Home Page --------------- #



t.mainloop() #Laisser la fenetre ouverte