from tkinter import * 

def textos_predefinidos(window):
    label1 = Label(window, text="Entrada", font="times 16 bold")
    label1.place(x=10, y=20)

    slabel1 = Label(window, text="Saída", font="times 16 bold")
    slabel1.place(x=460, y=20)

    # slabel2 = Label(window, text="Outro:", font="times 12")
    # slabel2.place(x=20 + 350, y=150)

    label2 = Label(window, text="Título:", font="times 12")
    label2.place(x=20, y=230.5 + 80)

    slabel2 = Label(window, text="Valor:", font="times 12")
    slabel2.place(x=20, y=262 + 80)


    tt_label = Label(window, text="Tipo de Transação", font="times 12 bold")
    tt_label.place(x=20, y=120)

    elabel1 = Label(window, text="Entrada/Saída", font="times 12 bold")
    elabel1.place(x=300, y=415)