import tkinter as tk

def menuCreate():
    menuRoot = tk.Tk()
    menuRoot.geometry("400x300")
    menuRoot.resizable(False, False)

    menuRoot.grid_columnconfigure(0, weight=1)

    titleLabel = tk.Label(menuRoot, text="Sistema de Cantina", font=("Arial", 20))
    titleLabel.grid(row=0, column=0)

    produtosBtn = tk.Button(menuRoot, width=20, height=4, text="Produtos", command="")
    produtosBtn.grid(row=1, column=0, padx=10, pady=5)
    vendasBtn = tk.Button(menuRoot, width=20, height=4, text="Vendas", command="")
    vendasBtn.grid(row=2, column=0, padx=10, pady=5)

    configBtn = tk.Button(menuRoot, width=20, height=4, text="Configurações", command="")
    configBtn.grid(row=3, column=0, padx=10, pady=5)




    menuRoot.mainloop()