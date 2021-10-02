import random
from string import ascii_lowercase, ascii_uppercase, digits

from gui import window, screen

while True:
    button, value = window.read()
    lenght = int(value["LEN"])
    symbol_choices = {'H': ascii_uppercase, "L": ascii_lowercase, "D": digits, "S": "!@#$%^&*()<>?/|+=-."}
    symbols = ''.join(v for k, v in symbol_choices.items() if value[k])
    if button in [None, "Quit"]:
        break
    elif button == "Generate!":
        screen = "".join(random.choices(symbols, k=lenght)) if symbols else "Please select generation settings ↑"
        window.FindElement("output").Update(screen)