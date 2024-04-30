from tkinter import * 
import pandas as pd

window = Tk()
window.geometry("700x500")

def haha(he):
    label2 = Label(window, text=he, font="times 28 bold")
    label2.place(x=350, y=210)

v = StringVar(window, "0")


def sel():
    print('')


label1 = Label(window, text="Entrada", font="times 16 bold")
label1.place(x=10, y=20)

R1 = Radiobutton(window, text="Doação", variable=v, value="Doação", command=sel)
R1.place(x=20,y=45)
R2 = Radiobutton(window, text="Mensalidade", variable=v, value="Mensalidade", command=sel)
R2.place(x=20,y=65)
R2 = Radiobutton(window, text="Ação", variable=v, value="Ação", command=sel)
R2.place(x=20,y=85)


label2 = Label(window, text="Título:", font="times 12")
label2.place(x=20, y=230)
e1 = Entry(window)
e1.place(x=75,y=230)


# sR1 = Radiobutton(window, text="Doação", variable=v, value="Doação", command=sel)
# sR1.place(x=20 + 340,y=45)
# sR2 = Radiobutton(window, text="Mensalidade", variable=v, value="Mensalidade", command=sel)
# sR2.place(x=20 + 340,y=65)
# sR2 = Radiobutton(window, text="Ação", variable=v, value="Mensalidade", command=sel)
# sR2.place(x=20 + 340,y=85)

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
tt_label.place(x=20, y=120)

tt_rb = Radiobutton(window, text="Conta Bancária/pix", variable=t, value="Conta Bancária/pix")
tt_rb.place(x=20,y=170)
tt_rb2 = Radiobutton(window, text="Dinheiro", variable=t, value="Dinheiro")
tt_rb2.place(x=20,y=150)

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
            
    print("aaaaaaa")
    dados = {"fluxo": fluxo, "tipo_entrada": tipo_entrada, "titulo": titulo, "nome_beneficiario": nome_beneficiario, "valor": valor}
    df = pd.read_csv('teste.csv')
    
    # df = df.append({'fluxo': fluxo, 'tipo_entrada': tipo_entrada, 'titulo': titulo, 'nome_beneficiario': nome_beneficiario}, ignore_index=True)

    df.loc[-1] = [fluxo, tipo_entrada, titulo, nome_beneficiario, valor]
    df.index = df.index + 1
    df = df.sort_index()
    # df['fluxo'].iloc[len(df)] = fluxo
    # df['tipo_entrada'].iloc[len(df)] = tipo_entrada
    # df['titulo'].iloc[len(df)] = titulo
    # df['nome_beneficiario'].iloc[len(df)] = nome_beneficiario
    df.to_csv('teste.csv')
    print(len(df))
    print(df.info())


e = StringVar(window, "0")
elabel1 = Label(window, text="Entrada/Saída", font="times 12 bold")
elabel1.place(x=380, y=415)

eR1 = Radiobutton(window, text="Entrada", variable=e, value="Entrada", command=sel)
eR1.place(x=380,y=435)
eR2 = Radiobutton(window, text="Saída", variable=e, value="Saída", command=sel)
eR2.place(x=380,y=455)


slabel2 = Label(window, text="Valor:", font="times 12")
slabel2.place(x=15, y=268)
e3 = Entry(window)
e3.place(x=75,y=268)

botao_gerar = Button(window, text='Gerar Gráficos', command = lambda: gera_df(e.get(), t.get(), e1.get(), v.get(), e3.get()) if e.get() == "Entrada" else gera_df(e.get(), t.get(), v2.get(), e2.get(), e3.get()))
botao_gerar.place(x=500,y=440)


botao_enviar = Button(window, text='Enviar')
botao_enviar.place(x=155,y=300)


botao_enviar = Button(window, text='Enviar')
botao_enviar.place(x=500,y=180)


slabel2 = Label(window, text="valor:", font="times 12")
slabel2.place(x=20 + 340, y=150)
e2 = Entry(window)
e2.place(x=75 + 340,y=150)


window.mainloop()









# Colocar visor de fluxo de caixa (diário)