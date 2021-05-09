# É onde fica o código para minha interface gráfica.
# Tudo que vai exixstr de visual ficara aqui.
# É principalmente aqui usaremos o PySimpleGUI.
from ExercicioByLearn.email_sender.view import get_window
import PySimpleGUI as sg
from ExercicioByLearn.utils import inner_element_space

lista = ["Administradores","Alunos"]

def get_layout():
    frame_list = [
        inner_element_space(600),
        [
            sg.Text("Selecione a lista:"),
            sg.Combo(lista, default_value = lista[1],key = "-List-"),
        ],
        [
            sg.Text("Criar uma lista:"),
            sg.In(key = "-ListName-"),
            sg.Button("Criar",key = "-Create-", size = (10, 1)),
        ],
        [
            sg.Button(
                "Deletar a lista",
                key = "-Delete-",
                size = (15, 1),
                pad = (5,(7,7)),
            ),
            sg.Button(
                "Mostrar contatos",
                key = "-Delete-",
                size = (15, 1),
                pad = (5,(7,7)),
            )
        ],
        inner_element_space(600),
    ]

    frame_import = [
        inner_element_space(600),
        [
            sg.Txt(
                "Selecione o arquivo (CSV):",
                tooltip = "cabeçalhos: name e email",
                ),
            sg.In(key = "-CSV-"),
            sg.FileBrowse(
                "Selecionar",
                file_types = (("CSV","*.csv"),),
                tooltip = "cabeçalho: name e email",
            ),
        ],
        [
            sg.Button(
                "Importar contatos",
                key = "-Import-",
                size = (15, 1),
                pad = (0,(7,7)),
            )
        ],
        inner_element_space(600),
    ]

    frame_add = [
        inner_element_space(600),
        [sg.Text("Insira um nome:"),sg.In(key = "-Name-")],
        [sg.Text("Insira um Email:"),sg.In(key = "-Email-")],
        [
            sg.Button(
                "Adicionar contato:",
                key = "-Add-",
                size = (15, 1),
                pad = (0,(7,7)),
            ),
        ],
        inner_element_space(600),
    ]

    layout = [
        [
            sg.Frame(
                "Cofigurações da lista",
                frame_list, element_justification = "c",
            )
        ],
        [
            sg.Frame(
                "Importar contatos",
                frame_import,
                element_justification = "c",
            )
        ],
        [
            sg.Frame(
                "Adicionar Contato",
                frame_add,
                element_justification = "c",
            )
        ],
        [
            sg.Button(
                "voltar",
                key = "-Back-",
                size = (15, 1),
                pad = (0, (7,7)),
            )
        ],
        inner_element_space(600),
    ]

    return layout

def get_window():
    sg.theme("DarkBlue14")
    return sg.Window(
        "Editor de lista",
        get_layout(),
        element_justification = "c",
        )