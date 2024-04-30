from tkinter import * 

class LabelText:
    def __init__(self, window=None, texto=None, tamanhoFonte=None):
        self.tela = window
        self.texto = texto
        self.fonte = tamanhoFonte
        # self.label = Label()
        

    def nova_label(self, pos_x, pos_y):
        place = Label(self.tela, text=self.texto, font=self.fonte)
        place.place(x=pos_x, y=pos_y)
