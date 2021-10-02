import random
from string import ascii_lowercase, ascii_uppercase, digits

from gui import window, screen

while True:
    symbols = set()
    button, value = window.read()
    lenght = value["LEN"]
    if button in [None, "Quit"]:
        break
    elif button == "Generate!":
        screen.format()
        screen = str(*[random.choice(list(symbols)) for _ in range(lenght)])
        window.FindElement("output").Update(screen)
    elif value["H"]:
        symbols.union(ascii_uppercase)
    elif value["H"] is False:
        symbols.intersection(ascii_uppercase)
    elif value["L"]:
        symbols.union(ascii_lowercase)
    elif value["L"] is False:
        symbols.intersection(ascii_lowercase)
    elif value["D"]:
        symbols.union(digits)
    elif value["D"] is False:
        symbols.intersection(digits)
    elif value["S"]:
        symbols.union(
            ["!", "@", "#", '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '|', "_", "+", "=", "-", "."])
    elif value["S"] is False:
        symbols.intersection(
            ["!", "@", "#", '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '|', "_", "+", "=", "-", "."])
