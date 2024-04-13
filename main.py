from tkinter import * 

window = Tk()
window.geometry("700x500")

def haha(he):
    label2 = Label(window, text=he, font="times 28 bold")
    label2.place(x=350, y=210)

v = StringVar(window, "0")


# for (text, value) in values.items():
#     Radiobutton(window, text = text, variable = v,
#         value = value)
# v.place(x=250,y=10)
def sel():
    haha(v.get())


label1 = Label(window, text="Entrada/Saída", font="times 12 bold")
label1.place(x=10, y=20)

R1 = Radiobutton(window, text="Entrada", variable=v, value="Entrada", command=sel)
R1.place(x=20,y=45)
R2 = Radiobutton(window, text="Saída", variable=v, value="Saída", command=sel)
R2.place(x=20,y=65)
# R2.pack( anchor = W )
label1 = Label(window, text="Tipo de Transação", font="times 12 bold")
label1.place(x=300, y=20)

R1 = Radiobutton(window, text="Conta Bancária/pix", variable=v, value="Conta Bancária/pix", command=sel)
R1.place(x=310,y=45)
R2 = Radiobutton(window, text="Dinheiro", variable=v, value="Dinheiro", command=sel)
R2.place(x=310,y=65)


window.mainloop()