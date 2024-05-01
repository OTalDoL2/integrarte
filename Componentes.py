 #             ==================================================================================           #
#               Desenvolvido por: Julio Cezar e Lucas Ramos                                                  #
#               Descricao: O objetivo desse arquivo é ter Widgets/Componentes                                #
#               e suas respectivas posições na tela                                                          #
#               Data de Inicio:             Versao: Alpha 1.0                                                #
 #             ==================================================================================           #


from tkinter import * 



def textos_predefinidos(window):
    titulo_entrada = Label(window, text="Entrada", font="times 16 bold")
    titulo_entrada.place(x=10, y=20)

    titulo_saida = Label(window, text="Saída", font="times 16 bold")
    titulo_saida.place(x=460, y=20)

    label_titulo = Label(window, text="Título:", font="times 12")
    label_titulo.place(x=20, y=230.5 + 80)

    label_valor = Label(window, text="Valor:", font="times 12")
    label_valor.place(x=20, y=262 + 80)


    titulo_tt = Label(window, text="Tipo de Transação", font="times 16 bold")
    titulo_tt.place(x=20, y=120)

    titulo_ent_saida = Label(window, text="Entrada/Saída", font="times 12 bold")
    titulo_ent_saida.place(x=300, y=415)

def show_campo_outros(button):
    button.pack()
    button.place(x=75 + 340,y=150)
def hide_campo_outros(button):
    button.pack_forget()
        


def radio_buttons(window, titulo_value, tipo_transacao, fluxo, e2): 
    

    tipo_entrada_doacao = Radiobutton(window, text="Doação", variable=titulo_value, value="Doação")
    tipo_entrada_doacao.place(x=20,y=45)
    tipo_entrada_mensalidade = Radiobutton(window, text="Mensalidade", variable=titulo_value, value="Mensalidade")
    tipo_entrada_mensalidade.place(x=20,y=65)
    tipo_entrada_acao_social = Radiobutton(window, text="Ação", variable=titulo_value, value="Ação")
    tipo_entrada_acao_social.place(x=20,y=85)

    tipo_saida_c_agua = Radiobutton(window, text="Conta de Água", variable=titulo_value, value="Conta de Água", command=lambda: hide_campo_outros(e2))
    tipo_saida_c_agua.place(x=356,y=45)
    tipo_saida_c_internet = Radiobutton(window, text="Internet", variable=titulo_value, value="Internet", command=lambda: hide_campo_outros(e2))
    tipo_saida_c_internet.place(x=484,y=45)
    tipo_saida_c_luz = Radiobutton(window, text="Conta de Luz", variable=titulo_value, value="Conta de Luz", command=lambda: hide_campo_outros(e2))
    tipo_saida_c_luz.place(x=356,y=65)
    tipo_saida_p_prof = Radiobutton(window, text="Pagamento Professores", variable=titulo_value, value="Pagamento Professores", command=lambda: hide_campo_outros(e2))
    tipo_saida_p_prof.place(x=484,y=65)
    tipo_saida_outros = Radiobutton(window, text="Outros", variable=titulo_value, value="Outros", command=lambda: show_campo_outros(e2))
    tipo_saida_outros.place(x=356,y=85)



    tipo_transacao_cb = Radiobutton(window, text="Conta Bancária/pix", variable=tipo_transacao, value="Conta Bancária/pix")
    tipo_transacao_cb.place(x=20,y=150)
    tipo_transacao_dinheiro = Radiobutton(window, text="Dinheiro", variable=tipo_transacao, value="Dinheiro")
    tipo_transacao_dinheiro.place(x=20,y=170)

    entrada = Radiobutton(window, text="Entrada", variable=fluxo, value="Entrada")
    entrada.place(x=300,y=435)

    saida = Radiobutton(window, text="Saída", variable=fluxo, value="Saída")
    saida.place(x=300,y=455)
