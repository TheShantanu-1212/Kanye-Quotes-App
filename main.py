import requests
from tkinter import *

ENDPOINT = "https://api.kanye.rest/"
RED = "#EA2F14"


def get_quote():
    """Fetch and display a random Kanye West quote from the API."""
    response = requests.get(url=ENDPOINT)
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


# ------------------------------------------------------UI SETUP------------------------------------------------------#

# Creating the main window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg=RED)

# Creating the canvas to display background image and quote
canvas = Canvas(width=300, height=414, bg=RED, highlightthickness=0)
background_img = PhotoImage(file="assets/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 20, "bold"),
    fill="black",
)
canvas.grid(row=0, column=0)

# Creating the Kanye button
kanye_img = PhotoImage(file="assets/kanye.png")
kanye_button = Button(
    image=kanye_img,
    highlightthickness=0,
    command=get_quote,
    bg=RED,
    activebackground="yellow",
)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()
