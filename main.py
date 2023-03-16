import requests
import random
from tkinter import *


def get_idea():
    form = ["education", "social", "recreational", "relaxation", "busywork", "diy"]

    parameters = {"type": random.choice(form),
                  "participants": 1}

    data = requests.get(url="http://www.boredapi.com/api/activity", params=parameters)
    data.raise_for_status()
    activity = data.json()["activity"]
    canvas.itemconfig(text, text=f"{activity}")


window = Tk()
window.title("Cure Boredom")
window.config(padx=50, pady=50, bg="#375362")

canvas = Canvas(width=300, height=250, bg="white")
text = canvas.create_text(150, 125, text="Let's do some thing...", font=("Arial", 20, "italic"), fil="#375362",
                          width=250)
canvas.grid(column=0, row=1, pady=10)

photo = PhotoImage(file="lets_do_something.png")

# category = Label(text=f"category:", font=("Arial", 12, "bold"), bg="#375362", fg="white")
# category.grid(column=1, row=0)

button = Button(image=photo, highlightthickness=0, command=get_idea)
button.grid(column=0, row=2)

window.mainloop()
