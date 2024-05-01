from tkinter import * 
import pandas as pd
from Componentes import textos_predefinidos, radio_buttons

# Tela do Tkinter
window = Tk()
window.geometry("700x500")

# Variaveis cujos valores serão definidos por RadioButtons 
titulo_value = StringVar(window, "0")
tipo_transacao = StringVar(window, "0")
fluxo = StringVar(window, "0")

# Variãveis de Entrada, funcionam Inputs de texto
entrada_titulo = Entry(window)
entrada_titulo.place(x=72,y=227.5 + 80)
valor = Entry(window)
valor.place(x=72,y=257 + 80)
entrada_opcional = Entry(window)


# Posiciona os textos em suas devidas posições
textos_predefinidos(window)

# Posiciona os RadioButtons em suas devidas posições
radio_buttons(window, titulo_value, tipo_transacao, fluxo, entrada_opcional)




# Após registrar os dados em um csv, ele vai limpar os campos, para que o usuário possa realizar seu próximo registro
def limpa_campos():
    fluxo.set(None)
    tipo_transacao.set(None)
    titulo_value.set(None)
    entrada_titulo.delete(0, 'end')
    entrada_opcional.delete(0, 'end')
    valor.delete(0, 'end')
    
#
def realiza_novo_registro(fluxo, tipo_entrada, titulo, nome_beneficiario, valor):

    if(fluxo != "Entrada"):
        print("nome_beneficiario", nome_beneficiario)
        print("titulo", titulo)
        if titulo != "" and nome_beneficiario == "":
            print("tudo, menos adicional")
            nome_beneficiario = 'Integrarte'
        else: 
            titulo = nome_beneficiario
            nome_beneficiario = 'Integrarte'

    arquivofinal = pd.read_csv('registro_integrarte.csv')

    dados_dict = {"fluxo": fluxo, "tipo_entrada": tipo_entrada, "titulo": titulo, "nome_beneficiario": nome_beneficiario, "valor": valor}
    dados_df = pd.DataFrame([dados_dict])
    dados = pd.concat([arquivofinal, dados_df], ignore_index=True)

    dados.to_csv('registro_integrarte.csv', index=False)
    limpa_campos()
    


             
botao_registro = Button(window, text='Registrar', command = lambda: realiza_novo_registro(fluxo.get(), tipo_transacao.get(), titulo_value.get(), entrada_titulo.get(), valor.get()) if fluxo.get() == "Entrada" else realiza_novo_registro(fluxo.get(), tipo_transacao.get(), titulo_value.get(), entrada_opcional.get(), valor.get()))
botao_registro.place(x=425,y=435)


window.mainloop()