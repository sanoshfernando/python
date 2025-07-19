from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
reset = False
timer = None  # <-- Added to allow cancelling after()

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, reset, timer
    reset = True
    reps = 0
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    label.config(text="TIMER", fg=GREEN, font=(FONT_NAME,50), bg=YELLOW)
    check_mark.config(text="")
    countdown(0)
    canvas.itemconfig(time_text, text=f"00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global  reps, reset
    reset = False
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps<8 and reps%2==1:
        countdown(work_sec)
        label.config(text="Work", fg=GREEN, font=(FONT_NAME,50), bg=YELLOW)
        check_mark.config(text="✔" * (reps// 2))
    elif reps<7:
        countdown(short_break_sec)
        label.config(text="Break", fg=PINK, font=(FONT_NAME, 50), bg=YELLOW)
        check_mark.config(text="✔" * (reps // 2))
    else:
        countdown(long_break_sec)
        label.config(text="Break", fg=RED, font=(FONT_NAME, 50), bg=YELLOW)
        check_mark.config(text="✔" * (reps // 2))
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(sec_countdown):
    global timer
    min_countdown = sec_countdown//60
    canvas.itemconfig(time_text, text=f"{min_countdown}:{sec_countdown % 60:02d}")
    if sec_countdown>0 and reset == False:
        timer = window.after(1000,countdown,sec_countdown-1)

    else:
        window.attributes('-topmost', True)
        window.update()
        window.attributes('-topmost', False)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME,50), bg=YELLOW)
label.grid(column=1,row=0)

canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)

time_text = canvas.create_text(100,120, text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,20))
check_mark.grid(column=1, row=3)

window.mainloop()
