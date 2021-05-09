# Onde estarão todas as funções deste pacote.
# Ele é quem vai coordenar este pacote.

def initialize():
    from ExercicioByLearn.email_sender import Email_Sender

    ems = Email_Sender()
    ems.enable_window()