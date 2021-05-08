# É onde fica o código para minha interface gráfica.
# Tudo que vai exixstr de visual ficara aqui.
# É principalmente aqui usaremos o PySimpleGUI.
import PySimpleGUI as sg

lista = ["Administradores", "Alunos"]

def get_layout():
    layout = [
    [
        sg.Text("Selecione seu Código"),
        sg.In(),
        sg.FileBrowse(
            "Selecione",file_types = (("Código Python", "*.py"),
            )
        ),
    ],
    [
        sg.Text("Selecione a lista de destinatários"),
        sg.Combo(lista, default_value = lista[1]),
    ],
    [
        sg.Text("Insira um Título: "),
        sg.In(key= "-Title-"),
    ],
    [
        sg.Text("Insira o conteúdo do E-mail: "),
        sg.In(key= "-Content-"),
    ],
    [
        sg.Button("Enviar", key= "-Send-"),
        sg.Button("Gerenciar listas", key= "-ListEditor-"),
    ],
    ]

    return layout


def get_window():
   return sg.Window(
       "Teste de janela", get_layout()
       )