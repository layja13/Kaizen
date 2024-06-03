from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


# Choicing a French word in the csv file
data = pandas.read_csv("./data/french_words.csv")
list_dict = data.to_dict(orient="records")
choice = random.choice(list_dict)

#functions
def change():
    global timer
    window.after_cancel(timer)
    choice = random.choice(list_dict)
    canvas.itemconfig(ima, image=image)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(text, text=choice["French"], fill="black", font=("Ariel", 60, "bold"))
    timer = window.after(3000, flip_card)

def remove():
    global choice, timer, list_dict, data
    list_dict.remove({"French": choice["French"], "English": choice["English"]})
    list_dict_csv = pandas.DataFrame(list_dict)
    list_dict_csv.to_csv("./words_to_learn.csv", index=False)
    data = pandas.read_csv("./words_to_learn.csv")
    list_dict = data.to_dict(orient="records")
    choice = random.choice(list_dict)

    window.after_cancel(timer)
    choice = random.choice(list_dict)
    canvas.itemconfig(ima, image=image)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(text, text=choice["French"], fill="black", font=("Ariel", 60, "bold"))
    timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(text, text=choice["English"], fill="white")
    canvas.itemconfig(ima, image=image_2)



window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

# Buttons
right_image = PhotoImage(file="./images/right.png")
left_image = PhotoImage(file="./images/wrong.png")
button_right = Button(image=right_image, highlightthickness=0, command=remove)
button_right.grid(row=1,column=2)
button_wrong = Button(image=left_image,background=BACKGROUND_COLOR, highlightthickness=0, command=change)
button_wrong.grid(row=1,column=3)


# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
image = PhotoImage(file = "./images/card_front.png")
image_2 = PhotoImage(file = "./images/card_back.png")
ima = canvas.create_image(400,268, image = image)
title = canvas.create_text(400,150, text="French", font=("Ariel", 30, "italic"))
text = canvas.create_text(400, 260, text=choice["French"], font=("Ariel", 60, "bold"))
canvas.grid(row=0,column=2, columnspan=2)


window.mainloop()
