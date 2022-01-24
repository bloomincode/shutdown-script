import os
import PySimpleGUI as sg

sg.theme('DarkPurple6')
font = ("Arial", 12)


quote = "Good night, good night!\nParting is such sweet sorrow;\nthat I shall say good night\ntill it be morrow."

layout = [[sg.Text(quote)],[sg.Button("Good Night"), sg.Cancel()]]

window = sg.Window("Good Night Sweetheart", layout, font=font, size=(290,120), element_justification='c')

while True:
    event, values = window.read()
    if event == 'Good Night':
        os.system("sudo shutdown -h now")
        break
    elif event == sg.WIN_CLOSED or event == 'Cancel':
        break
window.close()
