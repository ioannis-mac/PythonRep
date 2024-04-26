import tkinter as tki

def button_click1():
    label.config(text='Bouton 1 clique')

def button_click2():
    label.config(text='Bouton 2 clique')


fenetre = tki.Tk()
fenetre.title('Exemple de Side')

frame = tki.Frame(fenetre)
frame.pack()

button1 = tki.Button(frame, text='Bouton 1', command=button_click1)
button1.pack(side=tki.LEFT)

button2 = tki.Button(frame, text='Button 2', command=button_click2)
button2.pack(side=tki.LEFT)

fenetre.title('Hello Python')
fenetre.geometry('250x250')
label = tki.Label(fenetre, text="Bienvenue dans Tkinter")
label.pack()

fenetre.mainloop()