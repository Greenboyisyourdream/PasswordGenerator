import PySimpleGUI as gui

layout = [
    [gui.Text(text='Password generator', background_color="#900C3F", font=("Digital-7", 12),
              justification='left'),
     gui.Text(text="Lenght password:", background_color="#900C3F"),
     gui.OptionMenu(size=(15, 2), values=([i for i in range(1, 31)]), default_value=8, key="LEN")],
    [gui.Checkbox(text="High letters", background_color="#900C3F", default=False, key="H"),
     gui.Checkbox(text="Low letters", background_color="#900C3F", default=False, key="L"),
     gui.Checkbox(text="Digits", background_color="#900C3F", default=False, key="D"),
     gui.Checkbox(text="Spec. symbols", background_color="#900C3F", default=False, key="S"), ],

    [gui.InputText("", size=(50, 1), font=("Times New Roman", 10), background_color="white", text_color="black",
              key="output"), gui.Button(button_text="Generate!", size=(10, 1), button_color="red")]

]

window = gui.Window("Password generator", layout=layout, background_color="#900C3F", size=(420, 100))
