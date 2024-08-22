from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_NAME = "times new roman"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for l in range(randint(8, 10))]
    password_symbols = [choice(symbols) for s in range(randint(8, 10))]
    password_numbers = [choice(numbers) for n in range(randint(8, 10))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def error():
    messagebox.showerror(title="Oopsie", message="Please fill in all the boxes")


def save_data():
    website = website_input.get()
    EU = EU_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": EU,
            "password": password
        }
    }

    if len(website) == 0 or len(EU) == 0 or len(password) == 0:
        error()
    else:

        # is_sure = messagebox.askokcancel(title=website,
        #                                  message=f"These are your details\n"
        #                                          f"website:{website}\n"
        #                                          f"Email/Username:{EU}\n"
        #                                          f"Password:{password}")
        # if is_sure:
        try:
            with open("data.json", "r") as data_file:
                # data.write(f"/{website}/{EU}/{password}/\n")
                # .dump is to write in json
                # json.load is to read, but with open has to use "r"

                # reads old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                # updates old data with new data
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # writes using the new data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_details():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="you have not entered anything for that website")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"email: {email}\n"
                                                      f"password: {password}")
        else:
            messagebox.showinfo(title="ERROR", message="you have not entered anything for that website")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# website row
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=21)
website_input.grid(row=1, column=1, columnspan=1)
website_input.focus()

# Email/Username row
EU_label = Label(text="Username/email:")
EU_label.grid(row=2, column=0)
EU_input = Entry(width=35)
EU_input.insert(0, "nabilrobertdeniro@gmail.com")
EU_input.grid(row=2, column=1, columnspan=2)

# password row
password_label = Label(text="password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)
generate_button = Button(text="Generate password", command=generate_pass)
generate_button.grid(row=3, column=2)

# add button row
add_button = Button(text="add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

#search button
search_button = Button(text="search", width=13, command=find_details)
search_button.grid(row=1,column=2)

window.mainloop()
