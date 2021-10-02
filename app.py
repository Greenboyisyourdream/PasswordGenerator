import random
from string import ascii_lowercase, ascii_uppercase, digits

from gui import window, screen

while True:
    button, value = window.read()
    lenght = value["LEN"]
    symbols = ''
    if value["H"]:
        symbols += ascii_uppercase
    if value["L"]:
        symbols += ascii_lowercase
    if value["D"]:
        symbols += digits
    if value["S"]:
        symbols += '!@#$%^&*()<>?|+=-.'
    elif button == "Generate!":
        try:
            screen.format()
            screen = "".join(random.choices(list(symbols), k=int(lenght)))
            window.FindElement("output").Update(screen)
        except IndexError:
            screen = "Please select generation settings ↑"
            window.FindElement("output").Update(screen)