from tkinter import * 
import pandas as pd

window = Tk()
window.geometry("700x500")

titulo_value = StringVar(window, "0")


def sel():
    print('')


label1 = Label(window, text="Entrada", font="times 16 bold")
label1.place(x=10, y=20)

R1 = Radiobutton(window, text="Doação", variable=titulo_value, value="Doação", command=sel)
R1.place(x=20,y=45)
R2 = Radiobutton(window, text="Mensalidade", variable=titulo_value, value="Mensalidade", command=sel)
R2.place(x=20,y=65)
R2 = Radiobutton(window, text="Ação", variable=titulo_value, value="Ação", command=sel)
R2.place(x=20,y=85)


label2 = Label(window, text="Título:", font="times 12")
label2.place(x=20, y=110)
e1 = Entry(window)
e1.place(x=75,y=114)


v2 = StringVar(window, "")

slabel1 = Label(window, text="Saída", font="times 16 bold")
slabel1.place(x=460, y=20)

gastos = [ "Conta de Água", "Conta de Luz", "Internet", "Pagamento Professores", "outros"] #etc


select_begin = OptionMenu(window, v2, *gastos)
select_begin.pack()
select_begin.configure(border=0, bg="#c9c9c9", width=15, height=1)
select_begin.place(x=412,y=74)


slabel2 = Label(window, text="Outro:", font="times 12")
slabel2.place(x=20 + 340, y=110)
e2 = Entry(window)
e2.place(x=75 + 340,y=114)


t = StringVar(window, "0")

# R2.pack( anchor = W )
tt_label = Label(window, text="Tipo de Transação", font="times 12 bold")
tt_label.place(x=100, y=410)

tt_rb = Radiobutton(window, text="Conta Bancária/pix", variable=t, value="Conta Bancária/pix")
tt_rb.place(x=110,y=435)
tt_rb2 = Radiobutton(window, text="Dinheiro", variable=t, value="Dinheiro")
tt_rb2.place(x=110,y=455)

tipo_transacao = t.get()

print(t.get())

def gera_df(fluxo, tipo_entrada, titulo, nome_beneficiario, valor):
    if(fluxo != "Entrada"):
        if titulo != "" and nome_beneficiario == "":
            print("tudo, menos adicional")
        else: 
            titulo = nome_beneficiario
            nome_beneficiario = 'Integrarte'
            print("Apenas adicional")

    arquivofinal = pd.read_csv('me respeita.csv')

    dados_dict = {"fluxo": fluxo, "tipo_entrada": tipo_entrada, "titulo": titulo, "nome_beneficiario": nome_beneficiario, "valor": valor}
    dados_df = pd.DataFrame([dados_dict])
    dados = pd.concat([arquivofinal, dados_df], ignore_index=True)

    dados.to_csv('me respeita.csv', index=False)
    

e = StringVar(window, "0")
elabel1 = Label(window, text="Entrada/Saída", font="times 12 bold")
elabel1.place(x=300, y=415)

eR1 = Radiobutton(window, text="Entrada", variable=e, value="Entrada", command=sel)
eR1.place(x=300,y=435)

eR2 = Radiobutton(window, text="Saída", variable=e, value="Saída", command=sel)
eR2.place(x=300,y=455)
valor = Entry(window)
valor.place(x=425,y=240)
                        
botao_gerar = Button(window, text='Gerar Gráficos', command = lambda: gera_df(e.get(), t.get(), e1.get(),titulo_value.get(), valor.get()) if e.get() == "Entrada" else gera_df(e.get(), t.get(), v2.get(), e2.get(), valor.get()))
botao_gerar.place(x=425,y=435)


window.mainloop()