from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_']


def generate_pass():
    list_of_items = []

    [list_of_items.append(random.choice(letters)) for _ in range(random.randint(8, 10))]
    [list_of_items.append(random.choice(symbols)) for _ in range(random.randint(2, 4))]
    [list_of_items.append(random.choice(numbers)) for _ in range(random.randint(2, 4))]

    random.shuffle(list_of_items)
    new_password = "".join(list_of_items)
    password.set(new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_data.get()
    email_uname = email_uname_data.get()
    pw = password.get()
    new_data = {
        website: {
            "email": email_uname,
            "password": pw
        }
    }

    if website == "" or pw == "":
        messagebox.showerror(title="ERROR", message="You can't leave any fields empty.\n\
Please make sure to fill in any empty fields.")
        return

    is_fine = messagebox.askokcancel(title="SAVE",
                                     message="These are your credentials\nEmail/Username:{}\nPassword:{}\nContinue?"
                                     .format(email_uname, pw))

    if is_fine:
        try:
            with open("passwords.json", "r") as file:
                # Read old data
                data = json.load(file)

        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Update old data
            data.update(new_data)

            with open("passwords.json", "w") as file:
                # Save new data
                json.dump(data, file, indent=4)
        finally:
            website_data.delete(0, END)
            pw_data.delete(0, END)


# ---------------------------- SEARCH PASS ------------------------------- #


def search_pass():
    website = website_data.get()
    if website == "":
        return

    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(message="Database empty.", title="Error")
    else:
        if website in data:
            messagebox.showinfo(title="Details found.", message="Email:{}\nPassword:{}".format(
                data[website]["email"],
                data[website]["password"]))
        else:
            messagebox.showerror(title="Details not found", message="Details are not in our database")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Labels
label = Label(text="Website:")
label.grid(column=0, row=1)

label1 = Label(text="Email/Username:")
label1.grid(column=0, row=2)

label2 = Label(text="Password:")
label2.grid(column=0, row=3)

# Entries
website_data = Entry(width=36)
website_data.grid(column=1, row=1, columnspan=2)
website_data.focus()

email_uname_data = Entry(width=36)
email_uname_data.grid(column=1, row=2, columnspan=2)
email_uname_data.insert(0, "YOUR_DEFAULT_EMAIL")

password = StringVar()
pw_data = Entry(width=18, show="*", textvariable=password)
pw_data.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Search", highlightthickness=0, command=search_pass, width=8)
generate_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", highlightthickness=0, command=generate_pass)
generate_button.grid(row=3, column=2)
# generate_button.place(x=254, y=247)

save_button = Button(text="Add", width=30, highlightthickness=0, command=save)
save_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
