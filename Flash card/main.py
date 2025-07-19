from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


try:
    french_words = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    french_words=pandas.read_csv("data/french_words.csv")

to_learn = french_words.to_dict(orient="records")


def gen_word():
    global  flip_timer,current_card
    window.after_cancel(flip_timer)
    canvas.itemconfig(bg_img, image=front_img)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_word,text=current_card["French"],fill="black")
    canvas.itemconfig(canvas_title,text="French",fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_title,text="English",fill="white")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill = "white")
    canvas.itemconfig(bg_img,image=back_img)

def remove_card():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/to_learn.csv", index=False)
    gen_word()

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50, highlightthickness=0)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_img = PhotoImage(file="images/card_back.png")
front_img = PhotoImage(file="images/card_front.png")

bg_img = canvas.create_image(400,256,image=front_img)
canvas_title = canvas.create_text(400,150, text="Title", font=("Arial",40, "italic"))
canvas_word = canvas.create_text(400,260, text="Word", font=("Arial",60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
w_button = Button(image=wrong, highlightthickness=0,command=gen_word)
w_button.grid(row=1, column=0)
right = PhotoImage(file="images/right.png")
r_button = Button(image=right,highlightthickness=0,command=remove_card)
r_button.grid(row=1, column=1)

flip_timer = window.after(3000, func=flip_card)
gen_word()


window.mainloop()
