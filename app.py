import random
from string import ascii_lowercase, ascii_uppercase, digits

from gui import window, symbols, lenght

while True:
    button, value = window.read()
    if button in [None, "Quit"]:
        break
    elif button == "Generate!":
        screen = str(*[random.choice(symbols) for _ in range(lenght)])
        window.FindElement("output").Update(screen)
    elif value["H"]:
        symbols.extend([str(i) for i in ascii_uppercase])
    elif value["H"] is False:
        symbols.remove([str(i) for i in ascii_uppercase])
    elif value["L"]:
        symbols.extend([str(i) for i in ascii_lowercase])
    elif value["L"] is False:
        symbols.remove([str(i) for i in ascii_lowercase])
    elif value["D"]:
        symbols.extend([str(i) for i in digits])
    elif value["D"] is False:
        symbols.remove([str(i) for i in digits])
    elif value["S"]:
        symbols.extend(
            ["!", "@", "#", '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '|', "_", "+", "=", "-", "."])
    elif value["S"] is False:
        symbols.remove(
            ["!", "@", "#", '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '|', "_", "+", "=", "-", "."])
