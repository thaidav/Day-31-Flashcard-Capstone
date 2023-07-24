from tkinter import *
from json import *
from random import *
import pandas



BACKGROUND_COLOR = "#B1DDC6"
timer = None
FONT_NAME = "Courier"
STARTING_TIMER = 4
STOP = True
current_romaji = ""
current_word = ""
current_right_counter = 0
current_wrong_counter = 0
with open("Highscore.txt",mode="r") as score:
    Highscore = score.read()


# -------- Import Japanese -------- #

data = pandas.read_csv("Japanese_for_python.csv")
japanese_word = {row.romaji: [row.hiragana, row.katagana] for (index, row) in data.iterrows()}
japanese_romaji_list = [romaji for romaji in data["romaji"]]


# -------- Random Japanese-------- #

def random_japanese():
    global current_romaji
    global current_word
    random_romaji = choice(japanese_romaji_list)
    current_romaji = random_romaji
    current_word = japanese_word[random_romaji][randint(0,1)]
    canvas.itemconfig(word_label, text=current_word, fill="white")


# -------- Timer -------- #
# ------ Add a potential slider for a timer ---- #

def countdown(count):
    seconds = count
    if seconds > 3 and STOP:
        Label.config(timer_label, text=f"0{seconds}", fg="#95C063")
        print(seconds)
    elif count > 1 and STOP:
        Label.config(timer_label, text=f"0{seconds}", fg="#F49A1A")
        print(seconds)
    elif count > -1 and STOP:
        Label.config(timer_label, text=f"0{seconds}", fg="#F25A2C")
        print(seconds)
    if count > 0 and STOP:
        global timer
        global current_right_counter
        if current_right_counter < 100:
            timer = window.after(1000, countdown, count - 1)
        else:
            final_score()
    if count == 0:
        flip_the_card()

# ---------- Final Score --------- #

def final_score():
    global current_right_counter
    global current_wrong_counter
    global STARTING_TIMER
    total_seconds = (current_right_counter + current_wrong_counter)*STARTING_TIMER
    with open("Highscore.txt", mode="r") as score:
        current_highscore = score.read()
    with open("Highscore.txt", mode="w") as score:
        if total_seconds < int(current_highscore):
            score.write(str(total_seconds))


# ---------- Flip the Card --------- #

def flip_the_card():
    canvas.itemconfig(card_background, image=card_front, anchor="center")
    print("Done")
    canvas.itemconfig(word_label, text=current_word, fill="black")
    canvas.itemconfig(romaji_label, text=current_romaji, fill="black")
    check_answer()
    next_card()


#--------- Next Card ---------- #
def next_card():
    wait = window.after(2000, next_card_2)

def next_card_2():
    global STARTING_TIMER
    countdown(STARTING_TIMER)
    canvas.itemconfig(romaji_label, text="")
    canvas.itemconfig(card_background, image=card_back, anchor="center")
    random_japanese()
#---- to add : Next word, clear user input space


# --------- Check Answer -------- #

def check_answer():
    global current_right_counter
    global current_wrong_counter
    global current_romaji
    user_input_to_check = user_input.get()
    print (user_input_to_check)
    print (current_romaji)
    if user_input_to_check == current_romaji:
        current_right_counter +=1
    else:
        current_wrong_counter +=1
    Label.config(text_right_counter, text=current_right_counter)
    Label.config(text_wrong_counter, text=current_wrong_counter)
    print(f"{current_right_counter}, {current_wrong_counter}")



# -------- UI ---------- #

window = Tk()
window.title("Flash Card")
window.config(padx=0,
              pady=20,
              bg=BACKGROUND_COLOR)
window.geometry("900x800")

timer_label = Label(text="05",
                    font=(FONT_NAME, 47, "bold",),
                    highlightthickness=0,
                    bg=BACKGROUND_COLOR,
                    fg="#95C063")
timer_label.grid(column=1, row=0)

canvas = Canvas(width=800,
                height=534,
                bg=BACKGROUND_COLOR,
                highlightthickness=0)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400, 272, image=card_back, anchor="center")
canvas.grid(column=1, row=1, columnspan=1, padx=50)

word_label = canvas.create_text(400, 220,
                                text="字",
                                font=("Arial", 150, "bold"),
                                fill="White")
romaji_label = canvas.create_text(400, 380,
                                text="",
                                font=("Arial", 50, "bold"),
                                fill="White")

user_input = Entry(width=20,
                      bg="white",
                      fg="black",
                      highlightthickness=0,
                      insertbackground="black",
                   )
user_input.focus()
user_input.grid(column=1, row=2)

text_right = Label(text="RIGHT",
                    font=(FONT_NAME, 40, "bold"),
                    highlightthickness=0,
                    bg=BACKGROUND_COLOR,
                    fg="#95C063")
text_right.place(x=100, y=600)

text_right_counter = Label(text=current_right_counter,
                    font=(FONT_NAME, 60, "bold"),
                    highlightthickness=0,
                    bg=BACKGROUND_COLOR,
                    fg="black")
text_right_counter.place(x=140, y=650)



text_wrong = Label(text="WRONG",
                    font=(FONT_NAME, 40, "bold"),
                    highlightthickness=0,
                    bg=BACKGROUND_COLOR,
                    fg="#F25A2C")
text_wrong.place(x=650, y=600)

text_wrong_counter = Label(text=current_wrong_counter,
                    font=(FONT_NAME, 60, "bold"),
                    highlightthickness=0,
                    bg=BACKGROUND_COLOR,
                    fg="black")
text_wrong_counter.place(x=690, y=650)

text_highscore = Label(text="Highscore",
                    font=(FONT_NAME, 20, "bold"),
                    highlightthickness=0,
                    bg=BACKGROUND_COLOR,
                    fg="black")
text_highscore.place(x=690, y=00)

text_highscore_score = Label(text=f"{Highscore}s",
                    font=(FONT_NAME, 20, "bold"),
                    highlightthickness=0,
                    bg=BACKGROUND_COLOR,
                    fg="black")
text_highscore_score.place(x=728, y=30)



#
# next_img = PhotoImage(file="./images/right.png")
# next_button = Button(text="Next", command=next_card, image=next_img)
# next_button.pack()

random_japanese()
countdown(STARTING_TIMER)
window.mainloop()




