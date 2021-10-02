import random
from string import ascii_lowercase, ascii_uppercase, digits

from gui import window, screen

while True:
    symbols = set(ascii_uppercase)
    button, value = window.read()
    lenght = value["LEN"]
    if value["H"]:
        symbols.union(ascii_uppercase)
    else:
        symbols.intersection(ascii_uppercase)
    if value["L"]:
        symbols.union(ascii_lowercase)
    else:
        symbols.intersection(ascii_lowercase)
    if value["D"]:
        symbols.union(digits)
    else:
        symbols.intersection(digits)
    if value["S"]:
        symbols.union(
            ["!", "@", "#", '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '|', "_", "+", "=", "-", "."])
    else:
        symbols.intersection(
            ["!", "@", "#", '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '|', "_", "+", "=", "-", "."])
    if button in [None, "Quit"]:
        break
    elif button == "Generate!":
        screen.format()
        screen = "".join(random.choice(list(symbols)) for _ in range(int(lenght)))
        window.FindElement("output").Update(screen)