from tkinter import *
from tkinter import messagebox
import pyperclip

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


password_letters = [random.choice(letters) for new in range(nr_letters)]
password_symbols = [random.choice(symbols) for new in range(nr_symbols)]
password_numbers = [random.choice(numbers) for new in range(nr_numbers)]

password_list = password_letters+password_numbers+password_symbols
random.shuffle(password_list)

password = "".join(password_list)

def write_password():
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    email = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()

    if len(password) == 0 or len(website)==0:
        messagebox.showinfo(title="Oops", message="Please make sure non of the fields are empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail:{email}\n"
                                               f"Password: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as text_file:
                text_file.write(f"{website} | {email} | {password}\n")
                password_entry.delete(0, END)
                website_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row = 0, column= 1)

#Labels
website_label = Label(text="Website")
website_label.grid(row= 1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row= 2, column=0)
password_label = Label(text="Password")
password_label.grid(row= 3, column=0)

#text box
website_entry = Entry(width= 52)
website_entry.focus()
website_entry.grid(row= 1,column=1,columnspan=2,sticky="w")
email_entry = Entry(width=52)
email_entry.insert(0,"sanoshdemian@gmail.com")
email_entry.grid(row= 2,column=1,columnspan=2,sticky="w")
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1,sticky="w")
#Button
password_button= Button(text="Generate Password",command=write_password)
password_button.grid(row=3, column=2,sticky="w")
add_button = Button(text="Add",width=44, command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()