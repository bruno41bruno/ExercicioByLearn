# Arquivo usado para transformar a pasta em pacote.
# ele é sempre executado ao importar este pacote.
import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from ExercicioByLearn.email_sender import view
from ExercicioByLearn.list_editor.manager import initialize as init_list_editor

class Email_Sender():
    def __init__(self):
        self.window = None

    def instantiate(self):
        if self.window == None:
            self.window = view.get_window()

    def enable_window(self):
        self.instantiate()
        
        while True:
            event, values = self.window.read()

            if event == WIN_CLOSED:
                self.close_window()
                break

            if event =="-Send-":
                title = values["-Title-"]
                content = values["-Content-"]

                sg.Popup(
                    f"O Título  é: {title}\n O conteúdo é: {content}",
                    title = "E-mail",
                    )

            if event == "-ListEditor-":
                self.hide_window()
                init_list_editor(self)

    def close_window(self):
        if self.window is not None:
            self.window.close()
        self.window = None

    def hide_window(self):
        if self.window is not None:
            self.window.Hide()

    def unhide_window(self):
        if self.window is not None:
            self.window.UnHide()