from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"


def gen_word():
    with open("data/french_words.csv","r") as french_words:
        

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50, highlightthickness=0)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_img = PhotoImage(file="images/card_back.png")
front_img = PhotoImage(file="images/card_front.png")

canvas.create_image(400, 263, image=back_img)
canvas.create_image(400,256,image=front_img)
canvas.create_text(400,150, text="Title", font=("Arial",40, "italic"))
canvas.create_text(400,260, text="Word", font=("Arial",60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
w_button = Button(image=wrong, highlightthickness=0)
w_button.grid(row=1, column=0)
right = PhotoImage(file="images/right.png")
r_button = Button(image=right,highlightthickness=0)
r_button.grid(row=1, column=1)


window.mainloop()
