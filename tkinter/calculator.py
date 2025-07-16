from tkinter import *
window = Tk()
window.title("My First GUI Program")

window.config(padx=20, pady=20)
def click():
    miles = float(box.get())
    my_label3.config(text=miles*1.60934)

box = Entry(width=10)
box.grid(column=1, row=0)

my_label1 = Label(text="Miles")
my_label1.grid(column=2, row=0)

my_label2 = Label(text="Is equal to")
my_label2.grid(column=0, row=1)

my_label3 = Label(text="0")
my_label3.grid(column=1, row=1)

my_label4 = Label(text="Km")
my_label4.grid(column=2, row=1)

button = Button(text="Calculate",command=click)
button.grid(column=1, row=3)

window.mainloop()