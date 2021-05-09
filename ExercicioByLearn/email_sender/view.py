# É onde fica o código para minha interface gráfica.
# Tudo que vai exixstr de visual ficara aqui.
# É principalmente aqui usaremos o PySimpleGUI.
import PySimpleGUI as sg
from ExercicioByLearn.utils import inner_element_space

lista = ["Administradores", "Alunos"]

def get_layout():
    frame_campaign = [
        inner_element_space(500),
        [
            sg.Text("Selecione o código:"),
            sg.In(key = "-Code-", size = (30, 1)),
            sg.FileBrowse("Selecionar",
            file_types = (("Códigos Python", "*.py"),),
            size = (15,1),
            ),
        ],
        [
            sg.Text("Selecione a lista de Destinatários"),
            sg.Combo(lista, default_value = lista[1], key = "-Lists-"),
        ],
        inner_element_space(500),
    ]

    frame_email = [
        inner_element_space(500),
        [sg.Text("Insira um Título", font = ("Helvética 15"))],
        [sg.In(key = "-Title-", size = (62, 1))],
        [sg.Text("Insira o Conteúdo", font = ("Helvética 15"))],
        [sg.MLine(key = "-Content-", size = (60, 10))],
        inner_element_space(500),
    ]

    layout = [
        inner_element_space(500),
        [ 
            sg.Frame(
            "Configurações da campanha",
            frame_campaign,
            element_justification = "c"
            )
        ],
        [
            sg.Frame(
            "Configurações do e-mail",
            frame_email,
            element_justification = "c"
            )
        ],
        [
            sg.Button(
            "Enviar E-mail",
            key = "-Send-",
            size = (15, 1),
            pad = (10, (10,0)),
            ),
            sg.Button(
            "Gerenciar Listas",
            key = "-ListEditor-",
            size = (15, 1),
            pad = (10, (10,0)),
            )
        ],
        inner_element_space(500),

    ]

    return layout

def get_window():

    sg.theme("DarkBlue14")
    return sg.Window(
        "Enviador de E-mail",
        get_layout(),
        element_justification = "c",
        )