from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    label_1.config(text="Timer")
    canvas.itemconfig(text, text= "00:00")
    conteo = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global conteo
    if conteo == 0:
        label_1.config(text="Work")
    count_down(WORK_MIN * 60)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
def count_down(count):
    global conteo
    global timer
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    if count <= 0:
        conteo += 1
        if conteo % 3:
            r = int(conteo/3)
            check_mark.config(text=" ✔ "* (r+1))
        if conteo % 8 == 0:
            label_1.config(text="Break")
            count_down(LONG_BREAK_MIN * 60)

        elif conteo % 2 == 0 or conteo == 0:
            label_1.config(text="Work")
            count_down(WORK_MIN * 60)
        elif conteo % 2 != 0:
            label_1.config(text="Break")
            count_down(SHORT_BREAK_MIN * 60)
    canvas.itemconfig(text, text = f"{minutes}:{seconds}")



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(pady=50,padx=95, bg = YELLOW )


#Labels
label_1 = Label(text="Timer", font=(FONT_NAME, 45), highlightthickness=0, fg=GREEN, bg=YELLOW)
label_1.grid(row=1,column=2)

check_mark = Label(text=" ✔ ", fg=GREEN,font=50, highlightthickness=0, bg=YELLOW)
check_mark.grid(row=4 ,column=2)

#Buttons
button_1 = Button(text="Start", font=(FONT_NAME, 15), command=start_timer)
button_1.grid(row=3,column=1)

button_2 = Button(text="Reset", font=(FONT_NAME, 15), command=reset)
button_2.grid(row=3,column=3)


canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
image = PhotoImage(file = "tomato.png")
canvas.create_image(100,112, image = image)
text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=2,column=2)

conteo = 0


window.mainloop()