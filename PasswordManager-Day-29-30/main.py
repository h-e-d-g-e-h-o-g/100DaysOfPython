# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


def delete_details():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for char in range(nr_letters)]
    symbols_list = [random.choice(symbols) for char in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if website == "" or password == "":
        messagebox.showinfo(title="Error", message="You have left empty fields!")
    else:
        try:
            with open("data.json", "r") as file1:
                data = json.load(file1)
                data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        finally:
            delete_details()

def find_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found")
    else:
        website_list = data.keys()
        website_input = website_entry.get()
        if website_input in website_list:
            messagebox.showinfo(title=website_input, message=f"Email: {data[website_input]['email']}"
                                                             f"\nPassword: {data[website_input]['password']}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists")


my_canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.png")
my_canvas.create_image(100, 100, image=password_image)
my_canvas.grid(row=0, column=1, sticky=EW)
website_name = Label(text="Website:")
website_name.grid(row=1, column=0)
website_entry = Entry(width=28)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky=W, padx=2, pady=2)
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(row=1, column=1,sticky=E, padx=2, pady=2)
email = Label(text="Email/Username:")
email.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.insert(0, string="negiarpit2003@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW, padx=2, pady=2)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, padx=2, pady=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=W, padx=2, pady=2)
generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3, column=1, sticky=E, padx=2, pady=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, sticky=W, padx=2, pady=2)

window.mainloop()
