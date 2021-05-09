# É onde fica o código para minha interface gráfica.
# Tudo que vai exixstr de visual ficara aqui.
# É principalmente aqui usaremos o PySimpleGUI.
from ExercicioByLearn.email_sender.view import get_window
import PySimpleGUI as sg

def get_layout():
    return [
        [sg.Text("Olá")],
    ]

def get_window():
    return sg.Window("Editor de lista", get_layout())