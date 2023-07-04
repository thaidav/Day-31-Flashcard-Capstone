from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
timer = None
FONT_NAME = "Courier"
STARTING_TIMER = 5

# -------- Timer -------- #

def countdown(count):
    seconds = count
    if seconds > 3:
        Label.config(timer_label, text=f"0{seconds}")
        print(seconds)
    elif count > 1:
        Label.config(timer_label, text=f"0{seconds}", fg="#F49A1A")
        print(type(seconds))
    else:
        Label.config(timer_label, text=f"0{seconds}", fg="#F25A2C")
        print(seconds)
    if count > 0:
        timer = window.after(1000, countdown, count - 1)






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
cardback = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 272, image=cardback)
canvas.pack()

countdown(5)

window.mainloop()




