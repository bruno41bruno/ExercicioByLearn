# Arquivo principal a ser executado.
# Quando iniciamos o projeto  ele é o primeiro ao python executar.
# Nós usamos  para ser o ponto de entrada da aplicação.
from ExercicioByLearn.email_sender import view

import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED

def enable_window():
    window = view.get_window()

    while True:
        event, values = window.read()

        if event == WIN_CLOSED:
            window.close()
            break

enable_window()