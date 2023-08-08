from tkinter import *
import math
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
check = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


def start_time():
    global reps
    reps += 1
    if reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

def reset_time():
    global check, reps
    window.after_cancel(timer)
    # In order to cancel the effects of window.after()
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check = ""
    check_label.config(text=check)
    reps = 0
    # Here, I need to stop my countdown, in order to achieve it, I need to use window.after_cancel()
    # In its argument, I need to pass that result which is generated from window.after().

def count_down(count):
    count_time = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_time}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count-1)
        # Calling the function after 1000 milli sec.
    else:
        start_time()
        if reps % 2 == 0:
            global check
            check += "✔"
            check_label.config(text=check)
# Here, in order to get change the text on the canvas, for that, I need to tap into the item first through canvas.
# I can do it through itemconfig(), in that method, first i need to specify that item that i need to change.
# Second, I need to specify the property of that item, i need to change.
# Here, you can see my count value is still in int type not string. Because, i am using the count argument passed in the count_down().
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # highlightthickness is used to remove the edges of the canvas.
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # With fill property, we can change the color of the text.
canvas.grid(column=1, row=1)
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
start_button = Button(text="Start", highlightthickness=0, command=start_time)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_time)
reset_button.grid(column=2, row=2)
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)
# Here, we are going to use canvas widget. Canvas widget works like real life canvas.
# Where, we can put one object over another. Like drawing one object over another.
# Here, we are going to put image onto our program, then we are going to put text over that image.
# Now, how to create or put image on the canvas. For that, we need to use "create_image".
# create_image() needs the x and y positions of the image in order to place the image.
# Then, it takes the PhotoImage object as argument in order to specify which image needs to be drawn on the canvas.
# The PhotoImage() class makes easy to read through the file in order to hold that image at that file location.
# Here, we can't use another loop in order to make the window to wait. As, we have already mainloop().
# So, we would not reach to the mainloop() after running the another loop.
# Here, we are using after(), in order to make the window to wait for a second, and then, call the function passed
# in the method and then pass the arguments which are going to be passed in the function need to call up.
window.mainloop()