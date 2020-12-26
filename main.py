from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_random_pw():
    password = ey_password.get()
    if len(password) > 0:
        ey_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    ey_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = ey_website.get()
    email = ey_email.get()
    password = ey_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword:{password} \n Is it ok to save?")

        if is_ok:
            with open("pw.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                ey_website.delete(0, END)
                ey_password.delete(0, END)

            f = open("pw.txt", "r")
            print(f.read())
            f.close()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

lb_website = Label(text="Website:")
lb_website.grid(column=0, row=1)

lb_email = Label(text="Email/Username:")
lb_email.grid(column=0, row=2)

lb_password = Label(text="password:")
lb_password.grid(column=0, row=3)

ey_website = Entry(width=41)
ey_website.focus()
ey_website.grid(column=1, row=1, columnspan=2)

ey_email = Entry(width=41)
ey_email.insert(0, "bnb089757NE@gmail.com")
ey_email.grid(column=1, row=2, columnspan=2)

ey_password = Entry(width=24)
ey_password.grid(column=1, row=3)

btn_create_pass = Button(text="Generate Password", width=16, command=create_random_pw)
btn_create_pass.grid(column=2, row=3)

btn_add = Button(text="Add", width=41, command=save_password)
btn_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
