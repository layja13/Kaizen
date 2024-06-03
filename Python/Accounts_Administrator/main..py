from tkinter import *
from tkinter import messagebox
import random
import json

def check():
    email_name = entry_email.get()
    website_name = entry_website.get()
    password_name = entry_password.get()
    try:
        with open("data.CARjson") as data:
            json.load(data)

    except FileNotFoundError:
        messagebox.showinfo(title="Information",
                            message=f"No such file exists")

    else:
        with open("data.json") as file:
            data = json.load(file)
            for i in data:
                if i == website_name:
                    messagebox.showinfo(title="Information",
                                        message=f"Email:{data[website_name]['email']}\nPassword:{data[website_name]['password']}")
                    return
            messagebox.showinfo(title="Information",
                                message=f"No such data found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    list_complete = numbers_list + symbols_list + letters_list


    random.shuffle(list_complete)

    password = "".join(list_complete)
    entry_password.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email_name = entry_email.get()
    website_name = entry_website.get()
    password_name = entry_password.get()
    new_data = {
        website_name: {
                "email": email_name,
                "password": password_name,
            }
    }

    if len(email_name) == 0 or len(website_name) == 0 or len(password_name) == 0:
        messagebox.showinfo(title="Warning", message="Please, don't leave any box empty")
    else:
        try:
            with open("data.json", "r") as text_file:
                data = json.load(text_file)
                data.update(new_data)

            with open("data.json", "w") as text_file:
                json.dump(data, text_file, indent=4)

        except FileNotFoundError:
            with open("data.json", "w") as text_file:
                json.dump(new_data,text_file, indent=4)



    entry_website.delete(0, 'end')
    entry_password.delete(0, 'end')



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = image)
canvas.grid(row=0,column=1)

# Labels
website = Label(text="Website:")
website.grid(row=1, column=0)
email= Label(text="Email/Username:")
email.grid(row=2, column=0)
password = Label(text="Pasword:")
password.grid(row=3, column=0)

# Entries
entry_website = Entry(width=31)
entry_website.grid(row=1,column=1)
entry_website.focus()


entry_email = Entry(width=50)
entry_email.grid(row=2,column=1, columnspan=2)
entry_email.insert(0, "luislayja1@gmail.com")


entry_password = Entry(width=31)
entry_password.grid(row=3,column=1)


#Buttons
generate = Button(text="Generate Password", width=15, command=generator_password)
generate.grid(row=3,column=2)

add = Button(text="Add",width=44, command=save)
add.grid(row=4,column=1, columnspan=2)

search = Button(text="Search", width=15,  command=check)
search.grid(row=1, column=2)


window.mainloop()






