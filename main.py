from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_letter=[choice(letters) for _ in range(randint(8,10))]
    password_number=[choice(numbers) for _ in range(randint(2,4))]
    password_symbols=[choice(symbols) for _ in range(randint(2,4))]

    password_list=password_letter+password_number+password_symbols

    shuffle(password_list)

    password="".join(password_list)

    pyperclip.copy(password)

    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    # checking if all the fields are filed or not
    if website_entry.get() == '' or email_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror(message="Some field(s) empty!")

    else:
        if_yes=messagebox.askokcancel(message="The following entries will be added to list")
        if if_yes:
            data_file = open("data.txt", mode="a")
            data_file.write(
                f"{website_entry.get()} | {email_entry.get()} |{password_entry.get()} \n")
            data_file.close()
            
        
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas_logo = canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# labels
website_name = Label(text="Website: ")
website_name.grid(row=1, column=0)

email_name = Label(text="Email/Username: ")
email_name.grid(row=2, column=0)

password_name = Label(text="Password: ")
password_name.grid(row=3, column=0)

# entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0, "2pulkit2@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=16)
password_entry.grid(row=3, column=1)

# buttons
generate_password = Button(text="Generate Password",command=gen_password)
generate_password.grid(row=3, column=2)

add = Button(text="ADD", width=36, command=add_to_file)
add.config(pady=10)
add.grid(row=4, column=1, columnspan=2)
window.mainloop()
