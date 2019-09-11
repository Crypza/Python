#Roll a dice
#Generate a random number between 1 and 6
import random
from tkinter import *


window = Tk()
window.title("Crypza's dice roller")
window.geometry('350x200')

randomNumber = random.randint(1,6)

lbl = Label(window, text="Roll the dice!", font=("Arial bold", 25))
lbl.grid(column=0, row=0)

def clicked():
    randomNumber = random.randint(1,6)
    lbl.configure(text=randomNumber)
btn = Button(window, text="Roll again", command=clicked)
btn.grid(column=1, row=1)

window.mainloop()



#print("Hello and welcome to Crypza's dice-roller")

#try:
#    sides = int(input ("How many sides does your dice have?: "))

#except ValueError:
#    exit("Thats not a number.")

