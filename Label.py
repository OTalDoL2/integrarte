from tkinter import * 

class LabelText:
    def __init__(self, window=None, texto=None, tamanhoFonte=None, posicao=None):
        self.tela = window
        self.texto = texto
        self.fonte = tamanhoFonte
        self.posicao_x = posicao[0]
        self.posicao_y = posicao[1]
        self.label = Label()
        

    def nova_label(self):
        self.label(self.tela, text=self.texto, font=self.fonte)
        self.place(x=self.x, y=self.y)
        return self