from tkinter import *
import pandas
import random

FONT_TITLE = ("Ariel", 40, "italic")
FONT_TEXT = ("Ariel", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"
flip_timer = 5
current_card = {}
# Here, current_card is global variable, it is created in order to hold the current card(french-english pair)
def card_known():
    french_dict_list.remove(current_card)
    new_data = pandas.DataFrame(french_dict_list)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    generate_random_word()

def generate_random_word():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(french_dict_list)
    random_french_word = current_card['French']
    canvas.itemconfig(card_img, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_french_word, fill="black")
    flip_timer = window.after(3000, generate_translation)


def generate_translation():
    canvas.itemconfig(card_img, image=back_img)
    translated_word = current_card['English']
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=translated_word, fill="white")



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=FONT_TITLE)
card_word = canvas.create_text(400, 263, text="", font=FONT_TEXT)
canvas.grid(row=0, column=0, columnspan=2)
image_left = PhotoImage(file="images/wrong.png")
button_left = Button(image=image_left, highlightthickness=0, command=generate_random_word)
button_left.grid(row=1, column=0)
image_right = PhotoImage(file="images/right.png")
button_right = Button(image=image_right, highlightthickness=0, command=card_known)
button_right.grid(row=1, column=1)
try:
    with open("data/words_to_learn.csv") as f:
        data_french = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    with open("data/french_words.csv") as f:
        data_french = pandas.read_csv("data/french_words.csv")
finally:
    french_dict_list = data_french.to_dict(orient="records")
# "orient" is a parameter to the to_dict(), it can be set to various values such as "list", "series" etc.
# Here, we set "orient" to "records", It creates a list in which dictionaries are the elements.
# It creates the dictionary of column heading-value pair.

generate_random_word()

window.mainloop()
