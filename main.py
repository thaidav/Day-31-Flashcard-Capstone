from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
timer = None
FONT_NAME = "Courier"
STARTING_TIMER = 5
STOP = True

# -------- Timer -------- #

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
        timer = window.after(1000, countdown, count - 1)
    if count == 0:
        flip_the_card()


# ---------- Flip the Card --------- #

def flip_the_card():
    canvas.itemconfig(card_background, image=card_front, anchor="center")
    print("Done")
    canvas.itemconfig(language_label, text="English", fill="black")
    canvas.itemconfig(word_label, text="字", fill="black")
    canvas.itemconfig(romaji_label, text="zi3", fill="black")
    canvas.itemconfig(english_label, text="Word", fill="black")

#--------- Next Card ---------- #
def next_card():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(card_background, image=card_back, anchor="center")
    countdown(STARTING_TIMER)


# --------- From Chinese > Japanese -------- #

# -------- UI ---------- #

window = Tk()
window.title("Flash Card")
window.config(padx=0,
              pady=20,
              bg=BACKGROUND_COLOR)
window.geometry("900x800")

timer_label = Label(text="05",
                    font=(FONT_NAME, 47, "bold"),
                    highlightthickness=0,
                    bg=BACKGROUND_COLOR,
                    fg="#95C063")
timer_label.pack()

canvas = Canvas(width=800,
                height=534,
                bg=BACKGROUND_COLOR,
                highlightthickness=0)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400, 272, image=card_back, anchor="center")
canvas.pack()

language_label = canvas.create_text(400, 80, text="中文", font=("Arial", 20, "normal"), fill="White")
word_label = canvas.create_text(400, 210, text="字", font=("Arial", 50, "bold"), fill="White")
romaji_label = canvas.create_text(400, 270, text="zi3", font=("Arial", 20, "italic"), fill="White")
english_label = canvas.create_text(400, 400, text="word", font=("Arial", 40, "bold"), fill="White")

next_img = PhotoImage(file="./images/right.png")
next_button = Button(text="Next", command=next_card, image=next_img)
next_button.pack()

countdown(5)

window.mainloop()




