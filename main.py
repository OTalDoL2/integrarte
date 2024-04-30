from tkinter import * 
import pandas as pd
from Componentes import textos_predefinidos
# from LabelText import LabelText

window = Tk()
window.geometry("700x500")

titulo_value = StringVar(window, "0")




textos_predefinidos(window)

def sel():
    print('')


# label1 = Label(window, text="Entrada", font="times 16 bold")
# label1.place(x=10, y=20)

R1 = Radiobutton(window, text="Doação", variable=titulo_value, value="Doação")
R1.place(x=20,y=45)
R2 = Radiobutton(window, text="Mensalidade", variable=titulo_value, value="Mensalidade")
R2.place(x=20,y=65)
R2 = Radiobutton(window, text="Ação", variable=titulo_value, value="Ação")
R2.place(x=20,y=85)


def show_campo_outros(button):
    button.pack()
    button.place(x=75 + 340,y=150)
def hide_campo_outros(button):
    button.pack_forget()
        
e2 = Entry(window)

"Conta de Água", "Conta de Luz", "Internet", "Pagamento Professores", "outros"
R13 = Radiobutton(window, text="Conta de Água", variable=titulo_value, value="Conta de Água", command=lambda: hide_campo_outros(e2))
R13.place(x=356,y=45)
R23 = Radiobutton(window, text="Conta de Luz", variable=titulo_value, value="Conta de Luz", command=lambda: hide_campo_outros(e2))
R23.place(x=356,y=65)
R33 = Radiobutton(window, text="Internet", variable=titulo_value, value="Internet", command=lambda: hide_campo_outros(e2))
R33.place(x=484,y=45)
R43 = Radiobutton(window, text="Pagamento Professores", variable=titulo_value, value="Pagamento Professores", command=lambda: hide_campo_outros(e2))
R43.place(x=484,y=65)
R53 = Radiobutton(window, text="Outros", variable=titulo_value, value="Outros", command=lambda: show_campo_outros(e2))
R53.place(x=356,y=85)


# label2 = Label(window, text="Título:", font="times 12")
# label2.place(x=20, y=110)

# titulo
e1 = Entry(window)
e1.place(x=72,y=227.5 + 80)


v2 = StringVar(window, "")

# slabel1 = Label(window, text="Saída", font="times 16 bold")
# slabel1.place(x=460, y=20)

# gastos = [ "Conta de Água", "Conta de Luz", "Internet", "Pagamento Professores", "outros"] #etc


# select_begin = OptionMenu(window, v2, *gastos)
# select_begin.pack()
# select_begin.configure(border=0, bg="#c9c9c9", width=15, height=1)
# select_begin.place(x=412,y=74)


# slabel2 = Label(window, text="Outro:", font="times 12")
# slabel2.place(x=20 + 340, y=110)



t = StringVar(window, "0")
tt_rb = Radiobutton(window, text="Conta Bancária/pix", variable=t, value="Conta Bancária/pix")
tt_rb.place(x=20,y=150)
tt_rb2 = Radiobutton(window, text="Dinheiro", variable=t, value="Dinheiro")
tt_rb2.place(x=20,y=170)

tipo_transacao = t.get()

print(t.get())

def gera_df(fluxo, tipo_entrada, titulo, nome_beneficiario, valor):
    if(fluxo != "Entrada"):
        print("nome_beneficiario", nome_beneficiario)
        print("titulo", titulo)
        if titulo != "" and nome_beneficiario == "":
            print("tudo, menos adicional")
            nome_beneficiario = 'Integrarte'
        else: 
            titulo = nome_beneficiario
            nome_beneficiario = 'Integrarte'

    arquivofinal = pd.read_csv('registro integrarte.csv')

    dados_dict = {"fluxo": fluxo, "tipo_entrada": tipo_entrada, "titulo": titulo, "nome_beneficiario": nome_beneficiario, "valor": valor}
    dados_df = pd.DataFrame([dados_dict])
    dados = pd.concat([arquivofinal, dados_df], ignore_index=True)

    dados.to_csv('registro integrarte.csv', index=False)
    

e = StringVar(window, "0")
# elabel1 = Label(window, text="Entrada/Saída", font="times 12 bold")
# elabel1.place(x=300, y=415)

eR1 = Radiobutton(window, text="Entrada", variable=e, value="Entrada", command=sel)
eR1.place(x=300,y=435)

eR2 = Radiobutton(window, text="Saída", variable=e, value="Saída", command=sel)
eR2.place(x=300,y=455)

valor = Entry(window)
valor.place(x=72,y=257 + 80)
             
botao_gerar = Button(window, text='Gerar Gráficos', command = lambda: gera_df(e.get(), t.get(), titulo_value.get(), e1.get(), valor.get()) if e.get() == "Entrada" else gera_df(e.get(), t.get(), titulo_value.get(), e2.get(), valor.get()))
botao_gerar.place(x=425,y=435)


window.mainloop()