from tkinter import *

window = Tk()
window.title("Password manager")
#window.minsize(width=500, height=500)
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="mylocker.png")
canvas.create_image(100, 112, image=lock_img)
canvas.grid(column=1, row=0)

lb_website = Label(text="Website:")
lb_website.grid(column=0, row=1)

lb_email = Label(text="Email/Username:")
lb_email.grid(column=0, row=2)

lb_password = Label(text="password:")
lb_password.grid(column=0, row=3)

ey_website = Entry(width=30)
ey_website.grid(column=1, row=1)

ey_email = Entry(width=30)
ey_email.grid(column=1, row=2)

ey_password = Entry(width=10)
ey_password.grid(column=1, row=3)

btn_create_pass = Button(text="Generate Password", width=15)
btn_create_pass.grid(column=1, row=3)

btn_add = Button(text="Add", width=30)
btn_add.grid(column=1, row=4)

window.mainloop()