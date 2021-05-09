# Onde estarão todas as funções deste pacote.
# Ele é quem vai coordenar este pacote.

def initialize(email_sender):
    from ExercicioByLearn.list_editor import List_Editor

    ems = List_Editor(email_sender)
    ems.enable_window()