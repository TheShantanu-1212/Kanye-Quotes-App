import requests
from tkinter import *

ENDPOINT = "https://api.kanye.rest/"


def get_quote():
    """Fetch and display a random Kanye West quote from the API."""
    quote = requests.get(url=ENDPOINT).json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


# ------------------------------------------------------UI SETUP------------------------------------------------------#

# Creating the main window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Creating the canvas to display background image and quote
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="assets/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 20, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)

# Creating the Kanye button
kanye_img = PhotoImage(file="assets/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()
