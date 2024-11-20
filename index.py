import tkinter as tk

def sair():
    janela.destroy()

janela = tk.Tk()
janela.title("Exemplo de Labels")

info = "texto\nmassa"
rotulo = tk.Label(janela, text=info, justify="left")
rotulo.grid(row=0, column=0)

info2 = """aff peguei gripe
não gostei.
"""
rotulo2 = tk.Label(janela, text=info2, justify="right")
rotulo2.grid(row=1, column=0)

botao_sair = tk.Button(janela, text="Sair", command=sair)
botao_sair.grid(row=2, column=0)

janela.mainloop()